Currently we use [phing](https://www.phing.info) as build system and it makes it easy to run the unit tests or build the translation files for example.

# Execute phing

You can execute *phing* in the root directory of each repository. Depending on the repository, there are different *phing* targets available and you should have a look into the *build.xml* file to find out their name and what tasks they perform. In the Aimeos core, you can also execute *phing* in the subdirectories which contains a *build.xml* file too. Then, only the tasks related to these sub-directory are executed.

The most important targets for you are "setup" to populate the database and "test" to find out, if everything is still working as it should:
```bash
phing setup
phing test
```

If you would like to test the Aimeos core on your hardware you can use target "setupperf" to write performance test data to the database and browse through the ["Perfomance" site](../manual/working-with-sites.md) in the front end. You will have to activate the performance site in the [administration interface](../manual/working-with-sites.md).

# Aimeos core targets

The Aimeos core repository contains these targets:

all (or no target)
: Executes the setup, test and check targets

setup
: Sets up the database and writes the unit test data to the database

setupperf
: Sets up the database and writes the perfomance test data to the database

coverage
: Generates a [code coverage report](https://en.wikipedia.org/wiki/Code_coverage)

coverageext
: Generates a code coverage report for a specific extension directory given via "-Ddir=ext/<name>"

test
: Executes the unit tests

testext
: Executes the unit tests for a specific extension directory given via "-Ddir=ext/<name>"

testperf
: Executes the performance tests

check
: Executes the [code sniffer](https://pear.php.net/manual/en/package.php.php-codesniffer.php)

checkext
: Executes the code sniffer for a specific extension directory given via "-Ddir=ext/<name>"

doc
: Generates the API documentation from the PHPDoc blocks and the Wiki documentation for the configuration settings

clean
: Cleans up temporary files

i18n
: Extracts all strings that should be translated from the source files

build
: Generates all binary translation files and the compressed JS files

deploy
: Creates a .tar.bz2 package from the current repository

createext
: Creates new Aimeos extension
