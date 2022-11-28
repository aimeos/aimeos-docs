from setuptools import setup

setup(
    name='algolia',
    keywords='mkdocs algolia export',
    entrypoints={
        'mkdocs.plugins': [
            'algolia=aimeos.algolia:MarkdownExportPlugin'
        ]
    }
)
