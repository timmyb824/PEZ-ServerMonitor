# CHANGELOG



## v1.0.2 (2023-08-21)

### Build

* build: Add fetch-depth and tags options in Checkout step ([`494b354`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/494b3544ef11d652261b1cf831882f1b4fbbce4d))

### Chore

* chore(ci): update GH_TOKEN in Prepare package for release ([`6904024`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/6904024f5f3b0250ebda93031fe7d05807222d06))

* chore(ci): Add test installation step ([`4dac46f`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/4dac46fccaced6dbefd6eebcda2c490f20ddde9c))

* chore: update remove_dist setting to true ([`a7ba0ad`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/a7ba0adae48921fcb80e49165ca94923938da744))

* chore: remove old dists ([`2526643`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/252664318e2a8bbd70fe610c06829945cd1e09ca))

* chore(ci): fix GH_TOKEN secret name ([`ec32430`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/ec32430eb3f3b35f423da9671218365e96407fe5))

* chore: Update version to 1.0.1 and add release job ([`c693e38`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/c693e38ff3b1dd21277c064f04e689f704d4bd58))

### Ci

* ci: Run semantic-release for versioning and changelog ([`3156930`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/31569304e43ea8412a3aad99fd5d8f4cf99b4b26))

* ci: fix incorrect parameter name for repository-url ([`abc94c8`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/abc94c83e031c818e97e565d2d58707d3934e6c2))

### Fix

* fix(main): Fix imports and function calls ([`74733f2`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/74733f2e09417a9f6930bc02e83bd5ef95a34c01))

### Unknown

* Merge pull request #9 from timmyb824/ci/fix-gh-token ([`7e58917`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/7e58917e845622eeca09f895678f752ae5219aaa))

* Merge pull request #8 from timmyb824/ci/repo-url ([`1bf42a5`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/1bf42a554dd950029cb30e8acc9e4abe984ecbab))

* Merge pull request #7 from timmyb824/ci/repo-url ([`4b3ef45`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/4b3ef4518401c92b408edc2bb852fdb1ae82d804))

* Merge pull request #6 from timmyb824/ci/fix-ci ([`f1cf491`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/f1cf491631a3737cf5a402d516762c6a0c5723a3))

* Merge pull request #5 from timmyb824/ci/fix-auto-versioning ([`35f5175`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/35f51759c5a4e257cef6160b25e8653a03aafa19))


## v1.0.1 (2023-08-21)

### Chore

* chore(src): organized files into folders within src ([`6bf6c36`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/6bf6c3619be30340ee6e17c126c4b7ae61ed1e5d))

* chore(poetry): add doit package and other version bumps ([`07c2dc3`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/07c2dc3b3aebb654012bef1db96f9eb771bd4254))

* chore(tests): update import paths to account for new src folder structure ([`1888ec4`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/1888ec447d4d5837651b339dcb4a78608f92951c))

* chore: add distribution files for pez_servermonitor-1.0.0

feat(pyproject.toml): add pip-tools and pyinstaller as dependencies for tooling ([`cc52767`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/cc52767637e13597f8d7a78614842d75e34d4ed4))

* chore(pyproject.toml): update project version to 1.0.0 and add project description
chore(pyproject.toml): update python dependency to &gt;=3.11,&lt;3.13
chore(pyproject.toml): add pyinstaller as a tooling dependency
chore(requirements.txt): update distro, netifaces, psutil, ping3, and pyyaml dependencies to support python version &gt;=3.11,&lt;3.13
chore(requirements.txt): update tabulate dependency to support python version &gt;=3.11,&lt;3.13
fix(config_parser.py): remove None type hint from parse_config_file function return type
fix(config_parser.py): add UTF-8 encoding and mode=&#34;r&#34; to open function in parse_config_file function
fix(cpu.py): add encoding=&#34;UTF-8&#34; and mode=&#34;r&#34; to open function in get_cpu_cache_and_bogomips function
fix(latency.py): add &#34; ms&#34; suffix to latency value in check_ping function return statement
fix(latency.py): change exception variable name to exception in perform_ping function
fix(main.py): import os module
fix(main.py): update default value of --config argument in parse_args function
fix(main.py): update default value of config argument in print_all_info function
fix(services.py): change exception variable name to exception in check_a_service function ([`e002556`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/e002556ab5ccf55a5accd1c42d6039036846913b))

* chore(config.yaml): remove unused services from config.yaml file

chore(pyproject.toml): remove commented out code and unused classifiers from pyproject.toml file

chore(main.py): remove redundant comments and unused import statements in main.py file
feat(main.py): refactor main function to improve code readability and maintainability ([`7d32610`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/7d32610b587a6cc01e6c118b662ea64a42582430))

* chore(.pre-commit-config.yaml): add hooks for poetry-check, poetry-lock, and poetry-export from poetry 1.5.0
chore(.pre-commit-config.yaml): add arguments to poetry-export hook to generate requirements.txt file
chore(requirements.txt): update hashes for distro, netifaces, ping3, psutil, pyyaml, and tabulate packages for Python 3.11 compatibility ([`eff478a`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/eff478a911b08ac18e08afbba9f2d242cf68ce01))

* chore: Update Python version to 3.11.2 ([`e163c70`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/e163c707244dd18489db3046c6bc116d9290375e))

* chore: Update dependencies and requirements ([`eea9fdc`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/eea9fdcfcc6e9a875ce3b1affa11de2a6d437235))

* chore: update poetry version to 1.5.1 ([`ba68502`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/ba68502ce367e85d72f34c44b77c14a9c6f6d70c))

* chore: update build-test.yaml ([`7b934e0`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/7b934e0d039406dbcb9a81f9557149d5ef03c9fd))

* chore: Update command in build-test.yaml ([`ad2a050`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/ad2a050ae2d20a4156b717c063d79a841a170f00))

* chore: Update build-test.yaml ([`1d90930`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/1d9093084697e7457761da58bd6ee24c9294782a))

* chore: update build-test.yaml ([`3040bfe`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/3040bfeee61b78e1fa3f2ea72dc41d17e61bea46))

* chore: streamline script execution in workflow ([`a24d632`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/a24d632c6eda07eef95eed5134b03b75940f61fe))

* chore: Add environment variable for production environment ([`57973cf`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/57973cfcc09d0cfaf2f5a8741925fd886c1cec88))

* chore(ci): Remove unnecessary docker container check ([`213a78b`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/213a78bf210ed7fb0203a0ed0c93aac9d896c238))

* chore: Remove unnecessary ping hosts and add docker test cmd ([`2388483`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/238848335c054da4273196ade92ba5ebfc0c14a3))

* chore(build-test.yaml): update Python version to 3.10.12 ([`e0f5f89`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/e0f5f89fc2b6383239f296c20f48fc446d9fb274))

* chore: add ignore-pre-commit script ([`9a1bf52`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/9a1bf52d57cd0c7b482170822afbd8d5801148db))

### Ci

* ci(build-test.yaml): update when workflow runs and correct final step ([`dcca906`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/dcca9060ea05140324e78333c8c49cdaa65adef6))

### Feature

* feat(ci): add CI workflow for testing and publishing the app with python semantic versioning ([`2e6949d`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/2e6949d655acaed19f0938d44d80b0e02bc66814))

* feat(main.py): convert arg parse to click library ([`7010c60`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/7010c60e280b94e23235caebc38ccfec416d49c9))

* feat(main.py): convert arg parse to click library ([`f46074a`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/f46074a19d1db5bbe61d0d7fda8b23a7838fe29f))

* feat: add build and test GitHub Actions workflow ([`7041694`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/704169429bcc45247a3ec29e66d53e644355e34a))

### Fix

* fix(test_latency.py): update expected result in test_check_ping to match the actual format of the returned value
fix(test_latency.py): update expected results in test_perform_ping to match the actual format of the returned values ([`1a23667`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/1a23667aecb5b2383acd4bd761d301cd20b0ffc4))

* fix: set pyproject back ([`b6b05cb`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/b6b05cb1d84db6c43c07339e096c96074ec79d7c))

* fix(cpu): properly handle missing cpu information ([`000c8cc`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/000c8cce37acbf03e2c2f78750bca67fd774f563))

### Refactor

* refactor(src): clean up exceptions and prints; set PYTHONPATH ([`64968c2`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/64968c298a4198d995c9b695e764d2a0c4d0993f))

* refactor: stop program from exiting; precommit updates ([`ab30096`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/ab30096f7f296f25b808c76262dc8397c1966568))

### Test

* test: test packages pattern in pyproject ([`f695a93`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/f695a93fc0aa46fa71da905e46e25ac60a41b1c0))

* test: add mock functions for cpu info ([`124d5d0`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/124d5d00f178317450177c0a1ccf79b2a4010156))

* test(test): add many tests, new configs, and other changes ([`01d3ec4`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/01d3ec4d4e4a458634af24eae11f2482c2313b5c))

* test(test_config_parser): adds tests for parse_config_file function ([`39bbd05`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/39bbd05f9245251fc6221bea9d5f71b8f4b716e2))

### Unknown

* Merge pull request #4 from timmyb824/automate-versioning ([`dc3ddfa`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/dc3ddfae0016aac7f0dc2d312891a0d5f4d8ea2b))

* Merge pull request #3 from timmyb824:click

chore(tests): update import paths to account for new src folder struc… ([`3195740`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/31957404f9e7eff670bdc4986c1d89b92d9b94cc))

* Update README.md ([`f5afcb6`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/f5afcb6b04ad89dabc72d662ab66563bef4fddde))

* update(readme.md): add new gif ([`2422b63`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/2422b6380b476a096ebd28a7f8f2d8e41cd62bc5))

* Update README.md ([`898d83f`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/898d83f3477f5b256d1c1a6d1a4da7d010a05f12))

* update(main): fix latency test; update readme; add gif ([`27f6991`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/27f69914fc2b7bc5b2475ebc2543c26c583908ff))

* Create LICENSE ([`2615c77`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/2615c773e51e1de2d7b54ebf94fa2f8531a0a4dd))

* Merge pull request #2 from timmyb824/dockerize ([`3f17433`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/3f174337a4aa7ef6bbb098c52c0b7fb4144698a1))

* update(dockerize): add docker files and return UNKNOWN values for CPU info upon IOError ([`089e49c`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/089e49cd3a1e24bde78ec3b8aebc04ba59647195))

* Merge pull request #1 from timmyb824/improvements_v1 ([`4449d1b`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/4449d1b25bc717c470e62af4ac1306c700e6451f))

* UPDATE(improvements_v1): add custom exceptions ([`4c91c25`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/4c91c25cfcd3ddbca2fa4f3e2328c35588dda5ec))

* UPDATE(improvements_v1): add top processes by cpu mem ([`632a776`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/632a7764466d526217d9f10da46ce131f1b2131d))

* UPDATE(improvements_v1): move config file to args ([`5671fb7`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/5671fb73964a0cd08940c96d9a62d7718134e791))

* UPDATE(improvements_v1): refactor to add error handling, docstrings, and other improvements ([`808a5c2`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/808a5c29810ce7ea01aa8d553816879be3c50610))

* UPDATE(improvements_v1): add started readme ([`3283830`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/3283830156ca0fde900b960bcbbace09bbf5a4a1))

* init commit ([`edb8783`](https://github.com/timmyb824/PEZ-ServerMonitor/commit/edb8783b53a4c1d2569b64ad49b38097637fd930))
