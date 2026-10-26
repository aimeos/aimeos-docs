
# imagine

AI provider settings for generating images

```
admin/ai/imagine = 
```

* Type: array - Associative list of provider settings
* Since: 2026.10

The "provider" key contains the name of the Prisma provider used to
generate images for the "ai-imagine" MCP tool. The "model" key is only
used by providers which support selecting the model and all other keys
like "api_key" or "url" are passed to the provider as configuration,
e.g.

```
 ['provider' => 'openai', 'model' => 'gpt-image-1.5', 'api_key' => '...']
```

Don't store API keys in your code repository but use environment
variables or a local configuration file instead.

See also:

* admin/ai/write
* admin/ai/translate
* admin/ai/isolate
* admin/mcp/resource/ai/imagine

# isolate

AI provider settings for removing the background of images

```
admin/ai/isolate = 
```

* Type: array - Associative list of provider settings
* Since: 2026.10

The "provider" key contains the name of the Prisma provider used to
remove the image background for the "ai-isolate" MCP tool. The "model"
key is only used by providers which support selecting the model and all
other keys like "api_key" or "url" are passed to the provider as
configuration, e.g.

```
 ['provider' => 'removebg', 'api_key' => '...']
```

Don't store API keys in your code repository but use environment
variables or a local configuration file instead.

See also:

* admin/ai/write
* admin/ai/translate
* admin/ai/imagine
* admin/mcp/resource/ai/isolate

# translate

AI provider settings for translating texts

```
admin/ai/translate = 
```

* Type: array - Associative list of provider settings
* Since: 2026.10

The "provider" key contains the name of the Prisma provider used to
translate texts for the "ai-translate" MCP tool. The "model" key is only
used by providers which support selecting the model and all other keys
like "api_key" or "url" are passed to the provider as configuration,
e.g.

```
 ['provider' => 'deepl', 'api_key' => '...']
```

Don't store API keys in your code repository but use environment
variables or a local configuration file instead.

See also:

* admin/ai/write
* admin/ai/imagine
* admin/ai/isolate
* admin/mcp/resource/ai/translate

# write

AI provider settings for generating texts

```
admin/ai/write = Array
(
    [provider] => openai
    [model] => gpt-4o-mini
    [api_key] => test
)
```

* Default: 
```
Array
(
)
```
* Type: array - Associative list of provider settings
* Since: 2026.10

The "provider" key contains the name of the Prisma provider used to
generate texts for the "ai-write" MCP tool. The "model" key is only used
by providers which support selecting the model and all other keys like
"api_key" or "url" are passed to the provider as configuration, e.g.

```
 ['provider' => 'openai', 'model' => 'gpt-5.6-sol', 'api_key' => '...']
```

Don't store API keys in your code repository but use environment
variables or a local configuration file instead.

See also:

* admin/ai/translate
* admin/ai/imagine
* admin/ai/isolate
* admin/mcp/resource/ai/write