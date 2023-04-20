from setuptools import setup

setuptools.setup(
    name="algolia",
    version="0.1.2",
    description="Algolia export for MKDocs",
    keywords="mkdocs algolia export",
    packages=['algolia'],
    entry_points={
        'mkdocs.plugins': [
            'algolia=algolia:MarkdownExportPlugin'
        ]
    }
)
