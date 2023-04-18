from setuptools import setup, find_packages

setup(
    name="gpt-commit",
    version="0.1.0",
    description="AI-powered commit message generator and selector",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/gpt-commit",
    packages=find_packages(),
    install_requires=[
        # ここに必要な依存パッケージをリストしてください。
    ],
    entry_points={
        'console_scripts': [
            'gpt-commit=main:main'
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
