from setuptools import setup, find_packages

setup(
    name="gpt-commit",
    version="0.1.1",
    description="AIによるコミットメッセージ生成ツール",
    author="tkt-tmp",
    author_email="t.tampo@okorande.com",
    url="https://github.com/yourusername/gpt-commit",
    packages=find_packages(),
    install_requires=[
        "openai>=0.27.4",
        "langchain>=0.0.142",
        "transformers>=4.28.1",
        "torch>=2.0.0",
        "termcolor>=2.2.0",
        "prompt-toolkit>=3.0.38",
    ],
    entry_points={
        'console_scripts': [
            'gpt-commit=gpt_commit.main:main'
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
