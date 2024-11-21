
# openai

Configuration for ChatGPT API to generate texts

```
admin/jqadm/api/openai = 
```

* Type: array - Associative list of key/value pairs
* Since: 2022.10

Contains the settings for configuring the ChatGPT API. You have to configure at
least the API "key" created in your OpenAI account, all other settings are optional:

```
 [
   'key' => '<your-OpenAI-API-key>',
   'context' => 'You are a professional writer for product texts and blog articles and create descriptions and articles in the language of the input without markup'
   'model' => 'gpt-4o-mini',
   'url' => 'https://api.openai.com/v1/chat/completions',
 ]
```


# removebg

Configuration for image background removal service

```
admin/jqadm/api/removebg = stdClass Object
(
)
```

* Default: 
```
stdClass Object
(
)
```
* Type: array - Associative list of key/value pairs
* Since: 2024.10

Contains the settings for configuring the image background removal service.
Currently, only RemoveBG is supported and a RemoveBG API account is required to
use the service. You have to configure at least the API "key":

```
 [
   'key' => '<your-RemoveBG-API-key>',
 ]
```


# translate

Configuration for realtime online translation service

```
admin/jqadm/api/translate = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - Associative list of key/value pairs
* Since: 2019.10

Contains the settings for configuring the online translation service.
Currently, only DeepL is supported and a DeepL API account is required to
use the service. You have to configure at least the API "key", all other
settings are optional:

```
 [
   'key' => '<your-DeepL-API-key>',
   'url' => 'https://api.deepl.com/v2',
 ]
```
