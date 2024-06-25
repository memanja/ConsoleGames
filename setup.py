from setuptools import setup, find_packages

setup(
    name='play_it',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pyfiglet',
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'play-guessing-game=play_it.guessing_game:start_game',
            'list_games=play_it.list_games:list_games',
        ],
    },
    author='Manoj Shetty K',
    author_email='shettykmanojmask@gmail.com',
    description='Developed primarily for fun and learning purposes, this collection serves as a playground for '
                'budding developers and gamers alike. As such, you might encounter a few bugs along the way—consider '
                'them part of the adventure!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ConsoleGames',  # Update this with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
