from setuptools import setup
import os
import sys
import shutil

def create_platform_scripts():
    scripts = ['phar2062_update', 'phar2062_restore']
    script_dir = 'scripts'
    os.makedirs(script_dir, exist_ok=True)
    
    # Create scripts for both Unix and Windows
    for script in scripts:
        # Unix version
        with open(os.path.join(script_dir, f'{script}'), 'w') as f:
            f.write('#!/usr/bin/env sh\n')
            f.write('git fetch origin main\n')
            f.write('git clean -fd\n')
            if script == 'phar2062_restore':
                f.write('git reset --hard origin/main\n')
        
        # Windows version
        with open(os.path.join(script_dir, f'{script}.bat'), 'w') as f:
            f.write('@echo off\n')
            f.write('git fetch origin main\n')
            f.write('git clean -fd\n')
            if script == 'phar2062_restore':
                f.write('git reset --hard origin/main\n')

create_platform_scripts()

if sys.platform.startswith('win'):
    scripts = ['scripts/phar2062_update.bat', 'scripts/phar2062_restore.bat']
else:
    scripts = ['scripts/phar2062_update', 'scripts/phar2062_restore']

setup(
    name='phar2062',
    version='1.0',
    scripts=scripts,
    python_requires='>=3.6',
    install_requires=['build'],
)
