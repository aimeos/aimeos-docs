# Translation options

Aimeos uses Gettext for translations. The Gettext format is a widely used industry standard for translating content into all kind of languages and is supported by almost all translation tools. Translations consists of the translation source (.pot file, e.g. "lib-mshop.pot"), the translations for every language (.po files, e.g. "de.po") and the binary machine object file (e.g. "de").

If you want to replace only a few translations, you can easily do that by adding a configuration that will be used instead of the translations from the Gettext files. Please have a look into the articles about overwriting translations for your framework (Laravel, Symfony, etc.) or your application (TYPO3, etc.).

!!! note "New translations"
    To translate Aimeos to a new language or add missing translations for an existing language, please use the [Transifex website](https://www.transifex.com/aimeos/public/) instead. Theses translations will be added automatically to Aimeos in the next release.

# Gettext

Sometimes you need to overwrite some more translations because you use specific wording at your web site. Also, if you've created your own extension and classes which contains additional strings to translate, using the Gettext files is a much better approach.

Using Gettext, you can also create country specific translation files, e.g. "de_CH.po" resp. the "de_CH" binary file. If you configure your language in the Aimeos locale to be "de_CH" instead of "de", translations from the "de_CH" file will be used. If no translation is found in the "de_CH" file, the "de" file is used instead.

!!! warning
    You need the Gettext utilities (xgettext, msgfmt) for creating the .pot and binary files. In Windows environments, you have to install [Cygwin](https://www.cygwin.com/) and its Gettext package first.

## Replace translations

To replace existing Aimeos core translations in your own extension, you need to follow these steps:
1. Copy the existing .po file (e.g. de.po) to the same directory as in the core extensions, e.g. from "./ext/ai-client-html/client/i18n/de.po" to "./ext/myextname/client/i18n/de.po"
2. Change the translations you want to replace
3. Remove the strings/translations that should stay the same
4. Execute in the directory of the .po file: **msgfmt --statistics -c -o de de.po**

Repeat this for each language you need. There will be binary files without extension in the same directory afterwards. These are the ones that will be used to lookup translations first. If the binary file doesn't contain the translation for the requested string, the Aimeos core file will be used instead.

## Add new translations

Strings can only be translated if they are wrapped by one of these methods:

$context->getI18n()->dt( '<domain>', '<singular>' )
: Singular translations that can be used whenever the Aimeos context is available. That's not possible in item classes and templates

$context->getI18n()->dn( '<domain>', '<singular>', '<plural>', <number> )
: Singular or plural translation depending on the target language and the number argument. It can be used at the same locations like singular translations

$this->translate( '<domain>', '<singular>', '<plural>', <number> )
: Singular or plural translation in PHP templates. The plural and number argument are optional and if omitted, it will be treated as a singular translation

sprintf( '<singular>' )
: Strings wrapped by the sprintf() function will be extracted and added to the .pot files as well. This is mainly useful for exception messages which can be translated in the "catch" block afterwards

The "domain" argument determines the Gettext domain of the translation. In Aimeos translation domains like "mshop", "client" or "controller/jobs" are used. They correspond to the core and extension directory where the "./i18n/" subdirectory is located at. Translation domains separate translations into different files, so two translation domains can contain the same source string but different translations.

To translate new strings, follow these steps:
1. Change to the directory of your extension
2. Execute **phing -f phing.xml i18n** on the command line
3. Copy the new .pot file in the "./i18n/" directory to a .po file, e.g. de.po (two letter ISO code in lower case)
4. Translate the strings in the .po file
5. Execute **phing -f phing.xml build** on the command line

For each .po file there should be binary file without extension in the same directory afterwards. These binary files will be used to lookup the translation for the source string.

!!! note
    If the *phing* utility isn't available, you can also execute the commands (xgettext, msgfmt) yourself.
