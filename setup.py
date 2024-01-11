from setuptools import setup
import io

setup(
  name='shapesimilarity',
  version='1.0.0',
  author='Nelson Wenner',
  packages=['shapesimilarity'],
  url='https://github.com/nelsonwenner/shape-similarity',
  description='Quantify the similarity between two shapes/curves',
  long_description_content_type="text/markdown",
  long_description=io.open('README.md', encoding="utf-8").read(),
  keywords=['python', 'curve', 'frechet-distance', 'procrustes-analysis'],
  platforms=['any']
)
