
# openai

Configuration for ChatGPT API to generate texts

```
admin/jqadm/api/openai = 
```

* Type: array - Associative list of key/value pairs
* Since: 2022.10

Contains the required settings for configuring the ChatGPT API.
The necessary settings for ChatGPT are:

```
 [
   'key' => '<your-OpenAI-API-key>',
 ]
```


# translate

Configuration for realtime online translation service

```
admin/jqadm/api/translate = Array
(
)
```

* Default: Array
(
)

* Type: array - Associative list of key/value pairs
* Since: 2019.10

Contains the required settings for configuring the online translation service.
Currently, only DeepL is supported and a paid DeepL API account is required to
use the service. The necessary settings for DeepL are:

```
 [
   'url' => 'https://api.deepl.com/v2',
   'key' => '<your-DeepL-API-key>',
 ]
```
