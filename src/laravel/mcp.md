# Aimeos MCP server

The Aimeos Laravel package can expose its administration tools through the
[Model Context Protocol (MCP)](https://modelcontextprotocol.io/). MCP clients such as
ChatGPT, Claude, Codex and VS Code can then search and manage products, categories,
media, customers, orders and other shop data.

This guide uses [Laravel Passport](https://laravel.com/docs/passport) for OAuth 2.1
authentication. Passport is recommended for remote MCP clients because it supports
the browser-based authorization flow and dynamic client registration used by MCP.

!!! warning
    The MCP server provides administrative read and write operations. Only expose it
    over HTTPS and never remove the `auth:api` middleware from the route.

## Requirements

Before starting, make sure that:

* Aimeos is installed in a Laravel version supported by `laravel/mcp`
* the Laravel application has a login page, for example from Laravel Breeze
* the Aimeos `admin` gate is configured as described in the
  [Laravel setup guide](setup.md#configure-authentication)
* an Aimeos admin account exists
* the application is reachable through an HTTPS URL by the MCP client

You can create a superuser for the initial test if necessary:

```bash
php artisan aimeos:account --super admin@example.com
```

Use a limited admin or editor account for regular operation after verifying the
setup.

## Install Laravel MCP and Passport

Install the optional Laravel MCP transport:

```bash
composer require laravel/mcp:^0.9
php artisan vendor:publish --tag=ai-routes
```

The second command creates `routes/ai.php`. Aimeos registers its own MCP server
route, so this file is only needed for the OAuth discovery and registration routes.

Install Passport and its database tables and keys:

```bash
php artisan install:api --passport
```

## Configure the user model

Add Passport's `OAuthenticatable` contract and `HasApiTokens` trait to
`app/Models/User.php`. Merge these changes with the existing model instead of
replacing its other interfaces or traits:

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Laravel\Passport\Contracts\OAuthenticatable;
use Laravel\Passport\HasApiTokens;

class User extends Authenticatable implements OAuthenticatable
{
    use HasApiTokens, HasFactory, Notifiable;

    // Keep the existing model properties and methods.
}
```

## Add the Passport guard

Add an `api` guard using Passport to `config/auth.php`. Keep the existing `web`
guard because Passport uses it for the browser login and consent screen:

```php
'guards' => [
    'web' => [
        'driver' => 'session',
        'provider' => 'users',
    ],

    'api' => [
        'driver' => 'passport',
        'provider' => 'users',
    ],
],
```

## Register the OAuth routes

Add the OAuth routes to `routes/ai.php`:

```php
<?php

use Laravel\Mcp\Facades\Mcp;

Mcp::oauthRoutes();
```

This registers the OAuth discovery, dynamic client registration and authorization
routes required by MCP clients. Do not add another `Mcp::web()` call: the Aimeos
Laravel package already registers the Aimeos MCP server.

## Enable the Aimeos MCP route

The Aimeos endpoint is disabled by default. Enable it in `config/shop.php` and map
the route to Passport's `api` guard:

```php
'guards' => [
    // Keep other guard mappings.
    'mcp' => 'api',
],

'routes' => [
    // Keep the other Aimeos routes.
    'mcp' => [
        'prefix' => 'admin/{site}/mcp',
        'middleware' => ['api', 'auth:api'],
    ],
],
```

The `guards` mapping ensures that the authenticated Passport user is also added to
the Aimeos context used by the tools. The `{site}` placeholder selects the Aimeos
site the client will manage.

For the default site, the endpoint is:

```text
https://example.com/admin/default/mcp
```

Each site has its own endpoint. Replace `default` with the site's code when managing
another shop.

## Configure the consent screen

Publish Laravel MCP's Passport consent view:

```bash
php artisan vendor:publish --tag=mcp-views
```

Then tell Passport to use it in `app/Providers/AppServiceProvider.php`:

```php
use Laravel\Passport\Passport;

public function boot(): void
{
    // Keep the existing Aimeos Gate::define('admin', ...) configuration.

    Passport::authorizationView(function ($parameters) {
        return view('mcp.authorize', $parameters);
    });
}
```

When a new MCP client connects, Passport opens the application's login page and
then this view so the user can approve or reject access.

## Deploy the Passport keys

The Passport installation command creates signing keys for the local application.
Generate them when deploying a new production instance:

```bash
php artisan passport:keys
```

Do not commit the private key. Store both keys as deployment secrets or publish the
Passport configuration and provide `PASSPORT_PRIVATE_KEY` and
`PASSPORT_PUBLIC_KEY` through the environment.

After changing cached configuration or routes, clear the application caches:

```bash
php artisan optimize:clear
```

## Verify the server

Check that the Aimeos endpoint is registered:

```bash
php artisan route:list --name=aimeos_shop_mcp
```

The result should contain a `POST` route named `aimeos_shop_mcp` with a URI similar
to `admin/{site}/mcp`.

Also verify that the OAuth discovery routes exist:

```bash
php artisan route:list --path=.well-known
```

## Connect an MCP client

Use the full endpoint URL including the Aimeos site code:

```text
https://example.com/admin/default/mcp
```

The first connection opens a browser. Sign in with the Aimeos admin account and
approve the requested access.

### Codex CLI

Add the server to `~/.codex/config.toml` for all projects or `.codex/config.toml`
for one project:

```toml
[mcp_servers.aimeos]
url = "https://example.com/admin/default/mcp"
```

Then start the OAuth flow:

```bash
codex mcp login aimeos
```

### Claude Code

Register the remote HTTP server:

```bash
claude mcp add --transport http --scope user aimeos https://example.com/admin/default/mcp
```

### VS Code and GitHub Copilot

Create `.vscode/mcp.json`:

```json
{
  "servers": {
    "aimeos": {
      "type": "http",
      "url": "https://example.com/admin/default/mcp"
    }
  }
}
```

For web clients such as ChatGPT or Claude.ai, add a custom MCP app or connector and
enter the same endpoint URL.

## Permissions

OAuth authenticates the user but does not grant shop permissions by itself. Aimeos
applies two authorization levels:

1. The Laravel `admin` gate must allow the authenticated user to start the server.
2. Every MCP tool checks its resource permission below `admin/mcp/resource`.

Superusers can use all tools. The default MCP resource configuration grants
different operations to editor, admin and superuser groups. If you use a dedicated
`api` group, add it only to the resource operations that account requires.

The tools are discovered automatically by the client. Their names follow the
`resource-action` pattern, for example `product-search`, `product-save`,
`catalog-tree` and `order-get`.

## Troubleshooting

### The endpoint returns 404

Make sure `laravel/mcp` is installed, `shop.routes.mcp` is enabled and the URL
contains a valid Aimeos site code. Then run `php artisan optimize:clear` and check
the route list again.

### The endpoint returns 401

Confirm that the MCP route uses `auth:api`, the `api` guard uses the `passport`
driver and `routes/ai.php` contains `Mcp::oauthRoutes()`.

### The endpoint returns 403

The authenticated account either failed the Aimeos `admin` gate or lacks the
resource permission required by the tool. Test with a superuser first, then assign
only the required admin or editor permissions to the production account.

### No consent screen is shown

Confirm that the login routes work in a normal browser, the `mcp-views` were
published and `Passport::authorizationView()` is configured in the application
service provider.

For details about the underlying OAuth flow, refer to the
[Laravel MCP authentication documentation](https://laravel.com/docs/mcp#authentication)
and the [Laravel Passport documentation](https://laravel.com/docs/passport).
