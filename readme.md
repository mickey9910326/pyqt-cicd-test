# pyqt-cicd-demo

[![Build Status](https://travis-ci.com/mickey9910326/pyqt-cicd-demo.svg?branch=master)](https://travis-ci.com/mickey9910326/pyqt-cicd-demo)
[![codecov](https://codecov.io/gh/mickey9910326/pyqt-cicd-demo/branch/master/graph/badge.svg)](https://codecov.io/gh/mickey9910326/pyqt-cicd-demo)

## About

This project helps people set up their own a CI/CD pipline for your pyqt application.

This repo is a demo or example to develop a pyqt5 application with CI/CD. It use [travis-ci](https://travis-ci.com/) as a CI/CD service to test, build, and release pyqt application.

If you are lazy as me, just copy the `.travis.yml` to your project, and follow the steps below to build a CI/CD pipline for your pyqt application.

This repo use pytest and qtest to test a pyqt application on windows os, linux, and MacOS. After test, a  test report will be send to [codecov](codecov.io), and codecov will show the code coverage for pyqt application. NOTE: The tests done in this repo is quite simple, it will be more complicated in a real pyqt application.

A tag created will trigger deploy jobs. In deploy stage, travis-ci job will use pyinstaller to build an executable binary file on windows, linux, and MacOS. Then tar executable binary and library files together. At last, release the tar file to github.

## reference

- [QApplication instance/qtbot fixture causes travis-ci to abort and core dump
](https://stackoverflow.com/questions/56281631/qapplication-instance-qtbot-fixture-causes-travis-ci-to-abort-and-core-dump)

- [Extensive Python Testing on Travis CI](https://blog.travis-ci.com/2019-08-07-extensive-python-testing-on-travis-ci)

- [stackoverflow - How to deploy to github releases from travis](https://stackoverflow.com/questions/49119790/how-to-deploy-to-github-releases-from-travis)

- [stackoverflow - Travis-CI Auto-Tag Build for GitHub Release](https://stackoverflow.com/questions/28217556/travis-ci-auto-tag-build-for-github-release)

## Steps to build your own pipline

1. Copy `.travis.yml`, `requirements-test.txt` in this repo to your own repo. And enable your repo in [travis-ci](travis-ci.com)

2. Go to travis-ci setting page.

    ![](https://i.imgur.com/CYg56TD.png)

3. Set the `GITHUB_TOCKEN` environment variable in travis-ci setting page.

    Travis-ci use this tocken to get access for your github repo in deploy job.

    ![](https://i.imgur.com/TkPUdKO.png)

    You can generate your key at github.com/settings/tokens/new.

    ![](https://i.imgur.com/WmDRjdN.png)

    NOTE: This setting is for public repo. If you use pravite repo, just check the repo option for  pravite repo access.

4. Set the `CODECOV_TOKEN` environment variable in travis-ci setting page.

    In the last of test job, command `codecov` will use this tocken to get access your project on codecov.io and upload test report.

    ![](https://i.imgur.com/abdsrma.png)

    You can get the key of your project at the projecting setting page in codecov.io.

    app.codecov.io/gh/username/project-name/settings

    ![](https://i.imgur.com/m7DajdV.png)

5. Push a new commit to test it.

6. Create a new tag to test deploy jobs.

7. Add the badge to your project page, and open your favorite game!
