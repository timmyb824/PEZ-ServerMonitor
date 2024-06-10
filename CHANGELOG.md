# CHANGELOG



## v1.10.0 (2024-06-10)

### Feature

* feat: Add fallback using curl if ping fails due to &#34;Permission denied&#34; ([`c94410c`](https://github.com/timmyb824/python-SysInformer/commit/c94410ce58293af597ba83ee92e5cc6d37d5e2ee))

### Unknown

* Merge pull request #59 from timmyb824/fix/permission-issue-using-ping

feat: Add fallback using curl if ping fails due to &#34;Permission denied&#34; ([`21e58f0`](https://github.com/timmyb824/python-SysInformer/commit/21e58f0357453bff5c8ee7932ea069162a860705))


## v1.9.0 (2024-05-10)

### Feature

* feat: include mem usage from psutil ([`1394e4c`](https://github.com/timmyb824/python-SysInformer/commit/1394e4ca34f31da71d5e87c9eac3ade3c820f265))

### Unknown

* Merge pull request #58 from timmyb824/feat/include-psutil-mem

feat: include mem usage from psutil ([`7410dfb`](https://github.com/timmyb824/python-SysInformer/commit/7410dfb483074c772d85ab65e884f0ea09f96fe6))


## v1.8.1 (2024-04-29)

### Style

* style: update macos warning message and add message for linux ([`5e24a65`](https://github.com/timmyb824/python-SysInformer/commit/5e24a657912fcf4ae3f256e3845f30db25d9f2d0))


## v1.8.0 (2024-04-29)

### Feature

* feat: Update patch tags in pyproject.toml ([`e1010e2`](https://github.com/timmyb824/python-SysInformer/commit/e1010e2df40262c35faf9f759d8048b09347a1c7))

### Refactor

* refactor(system.py): remove commented-out code and unused imports for cleaner codebase
feat(system.py): improve support for retrieving distribution version for Linux systems
feat(system.py): add handling for unsupported operating systems in get_last_boot_time() and get_system_uptime() functions
refactor(system.py): remove commented-out code and unused imports
test(system.py): remove commented-out test cases and TODOs for missing tests ([`36a289e`](https://github.com/timmyb824/python-SysInformer/commit/36a289e8e40fdf84074c392f20a49fe33e5ab9a7))

### Unknown

* Merge pull request #57 from timmyb824/refactor/improve-dist-version

Merge pull request #56 from timmyb824/refactor/system-info ([`5abc0a3`](https://github.com/timmyb824/python-SysInformer/commit/5abc0a332c974755c3d9732e7cd9a6650d689441))


## v1.7.0 (2024-04-29)

### Feature

* feat(system.py): add support for retrieving last boot time as a date and time string
feat(system.py): improve error handling and return meaningful messages for obtaining last boot time
feat(system.py): add function to get system uptime as a string
test(system.py): add tests for retrieving last boot time on macOS and Linux platforms ([`46c4c3b`](https://github.com/timmyb824/python-SysInformer/commit/46c4c3b5a73fe90524d4aea783218cc1f6a1d3c1))

* feat: Add distro module to get system information and update system uptime calculation ([`36186d3`](https://github.com/timmyb824/python-SysInformer/commit/36186d3ab674c0861de05fd879faa9fd5fc49078))

### Fix

* fix(system.py): remove unused import statement for distro package
feat(system.py): import distro package within the Linux-specific block to ensure it is only imported when needed
feat(test_system.py): refactor test_get_system_uptime to include separate test cases for Linux and Darwin systems
feat(test_system.py): add skipif decorators to test_get_system_uptime_linux and test_get_system_uptime_darwin
feat(test_system.py): refactor test_get_user_count_unix to include multiple test cases with parameters
feat(test_system.py): refactor test_get_system_info to include separate test cases for Linux and Darwin systems ([`322ed74`](https://github.com/timmyb824/python-SysInformer/commit/322ed744def8333776a4d78b4b05165234828922))

### Refactor

* refactor: Simplify retrieving last boot date in system information ([`e15fd83`](https://github.com/timmyb824/python-SysInformer/commit/e15fd8320dcc11e4b8076f827de1d1a643a88da5))

* refactor(system.py): rename get_last_boot_time_macos to get_last_boot_time and add support for retrieving last boot time on non-Darwin systems
feat(system.py): add logic to retrieve last boot time using &#39;uptime -s&#39; command on non-Darwin systems
test(system.py): add tests for get_last_boot_time function for both Darwin and non-Darwin systems ([`31b0063`](https://github.com/timmyb824/python-SysInformer/commit/31b006393d80e61695378703ae0bbba9a4b41f2c))

### Unknown

* Merge pull request #56 from timmyb824/refactor/system-info

refactor/system info ([`aab0662`](https://github.com/timmyb824/python-SysInformer/commit/aab066216bfa6f292129be3e605aa51afba78276))

* Update README.md ([`7fbc4a3`](https://github.com/timmyb824/python-SysInformer/commit/7fbc4a3e200edb4b4dbb4e33535a6c99c7abb239))


## v1.6.0 (2024-04-11)

### Chore

* chore(.gitignore): add .plandex/ and PLANDEX.md to the .gitignore file
feat(cpu.py): add function to get CPU processor information and refactor get_cpu_info
feat(memory.py): add function to get total memory usage of all processes on macOS
feat(memory.py): add function to show warning message for macOS memory calculation ([`c24797e`](https://github.com/timmyb824/python-SysInformer/commit/c24797e13f5f985a012134ec15a455ac864e344d))

### Documentation

* docs: Update installation instructions with pyenv upgrade tip ([`b64914f`](https://github.com/timmyb824/python-SysInformer/commit/b64914ffd776bf00ceff74cab223ff6ed07f05b1))

### Feature

* feat(test_cpu.py): add platform check for Intel and Apple M3 Pro processors to skip tests if not running on the required processor
refactor(test_cpu.py): improve parametrize ids for better readability
refactor(test_memory.py): remove unused parse_vm_stat_output function to clean up codebase ([`f7f6170`](https://github.com/timmyb824/python-SysInformer/commit/f7f6170ee3f3e587b4e86cb792e7e5ee605cf43c))

### Unknown

* Merge pull request #55 from timmyb824/refactor/improve-macos-mem

refactor/improve macos mem ([`12ebf9a`](https://github.com/timmyb824/python-SysInformer/commit/12ebf9ad92779f0cb484ffc2b31a868d6cb6af63))


## v1.5.0 (2024-04-09)

### Feature

* feat(core/memory.py): add support for retrieving memory information on macOS using &#39;vm_stat&#39; and &#39;sysctl&#39; commands
feat(core/memory.py): implement function to parse &#39;vm_stat&#39; output for macOS memory info
feat(test_memory.py): add tests for calculate_memory_usage and parse_vm_stat_output functions ([`38e9970`](https://github.com/timmyb824/python-SysInformer/commit/38e9970db2ddb6fc566dba890de0c11a8f0d745d))


## v1.4.0 (2024-04-09)

### Feature

* feat: Add version command to tool&#39;s CLI options ([`6f0a575`](https://github.com/timmyb824/python-SysInformer/commit/6f0a575f738d401ef219463bb3cdf7f8ac43fb32))

* feat: Add version command to print tool&#39;s version ([`a0f251c`](https://github.com/timmyb824/python-SysInformer/commit/a0f251c682471dbb0435f01451cfc9f673894a51))

### Unknown

* Merge pull request #54 from timmyb824/feat/add-version-cmd

feat: Add version command to print tool&#39;s version ([`61ee675`](https://github.com/timmyb824/python-SysInformer/commit/61ee6758d87410f68db329312504d8bec5b86337))


## v1.3.0 (2024-04-09)

### Build

* build: Update GitHub Actions setup-python and cache actions to latest versions ([`b9fcc65`](https://github.com/timmyb824/python-SysInformer/commit/b9fcc65144894b14c263a150ae055a06b36f9c7f))

### Chore

* chore: Update test_cpu.py to fix broken test ([`04713c1`](https://github.com/timmyb824/python-SysInformer/commit/04713c17f44176204014d27506fadda894193a2a))

### Feature

* feat(constants.py): add constants file with common paths and URLs for better organization and reusability
refactor(containers.py): update print_running_containers function to handle empty containers list case
refactor(cpu.py): improve get_cpu_cache_and_bogomips function to provide clearer messages and handle macOS cache retrieval
refactor(cpu.py): update print_cpu_info function to only print CPU temperature on Linux systems
refactor(networking.py): update import statement for GET_WAN_IP constant
refactor(main.py): update import statement for CONFIG_PATH_DEFAULT constant

feat(test_cpu.py): add tests for get_cpu_cache_and_bogomips, get_cpu_info, get_cpu_usage, get_load_average, get_process_count, get_system_temperature functions to improve code coverage and ensure functionality ([`4feba54`](https://github.com/timmyb824/python-SysInformer/commit/4feba54edde0742afa3dc4d742151d4a5fbb1e6e))

### Refactor

* refactor(system.py): refactor get_system_info function to improve readability and maintainability
feat(system.py): add support for macOS last boot time retrieval and system uptime calculation
feat(system.py): add function to count user directories in Unix systems
feat(main.py): comment out check_os function to prevent unnecessary output and delay

feat(test_system.py): refactor test_system.py to use pytest fixtures and improve test readability and maintainability ([`e33d9a1`](https://github.com/timmyb824/python-SysInformer/commit/e33d9a1d506e476bc513f73decb8a4771745d99e))

### Unknown

* Merge pull request #53 from timmyb824/feat/add-support-for-macos

refactor(system.py): refactor get_system_info function to improve rea… ([`846520f`](https://github.com/timmyb824/python-SysInformer/commit/846520fd9892c2bf490b5803263431541268d180))


## v1.2.15 (2023-11-26)

### Chore

* chore(.pre-commit-config): update sourcery version to v1.11.0
chore(.pre-commit-config): update pre-commit-hooks version to v4.5.0
chore(.pre-commit-config): update black version to 23.10.1
chore(.pre-commit-config): update ripsecrets version to v0.1.7
chore(pyproject): update sourcery version to v1.11.0
chore(requirements): update psutil version to 5.9.6 ([`b427b22`](https://github.com/timmyb824/python-SysInformer/commit/b427b228b1d0f4fcf9c834a99e75aec813c98acc))

### Ci

* ci: add trufflehog pre-commit and other updates

git commit -m chore(.pre-commit-config.yaml): update sourcery version to v1.14.0
chore(.pre-commit-config.yaml): update black version to 23.11.0
chore(.pre-commit-config.yaml): update poetry version to 1.7.0
chore(.pre-commit-config.yaml): update conventional-pre-commit version to v3.0.0
feat(.pre-commit-config.yaml): add trufflehog hook to detect secrets in the code during commit stage ([`5da0858`](https://github.com/timmyb824/python-SysInformer/commit/5da085897e070301f88ee48d9bba02ec9dffa658))


## v1.2.14 (2023-09-29)

### Chore

* chore(pyproject): update python dependency version to &gt;=3.9 for compatibility
chore(requirements): update python dependency version to &gt;=3.9 for compatibility ([`817bf1d`](https://github.com/timmyb824/python-SysInformer/commit/817bf1dea99296843207e1487f9c8ea75b1b70ee))

* chore: add new hook ripsecrets and other tweaks to the configs ([`67d4f35`](https://github.com/timmyb824/python-SysInformer/commit/67d4f359066efb0352fb180b0d47a4f9265a215d))

### Ci

* ci: add breaking change commit type ([`83ccb5e`](https://github.com/timmyb824/python-SysInformer/commit/83ccb5ea907d6b381e7af0282cff45fb38148133))

### Unknown

* Merge pull request #52 from timmyb824/ci/force-vesion-update ([`2c5eb25`](https://github.com/timmyb824/python-SysInformer/commit/2c5eb25b1ae803a67b1fa913a0297f6ab1777004))

* Merge pull request #51 from timmyb824/chore/update-python-version ([`0995ec4`](https://github.com/timmyb824/python-SysInformer/commit/0995ec434c9f18e84aa006501336d01df17f5829))

* Merge pull request #50 from timmyb824/chore/add-pre-commit-hook ([`5f03dcf`](https://github.com/timmyb824/python-SysInformer/commit/5f03dcfa713977ce7949e3df8e9fa151c92c3ed8))


## v1.2.13 (2023-08-31)

### Fix

* fix: add click dependency ([`9beba8b`](https://github.com/timmyb824/python-SysInformer/commit/9beba8b49d8f9e0e27b275a524252962422fb886))

### Unknown

* Merge pull request #49 from timmyb824/fix/missing-click-dep ([`3b1d8bf`](https://github.com/timmyb824/python-SysInformer/commit/3b1d8bfdcc957ec6816ff6f3fc0f1eb6218d1542))


## v1.2.12 (2023-08-30)

### Fix

* fix: ensure default config is created when folder does not already exist ([`b0d7142`](https://github.com/timmyb824/python-SysInformer/commit/b0d7142ba7f5901ef775045d11aec139b023b694))

### Unknown

* Merge pull request #48 from timmyb824/fix/config-path-creation ([`3ebec0c`](https://github.com/timmyb824/python-SysInformer/commit/3ebec0c4207f474a2573b326b3516973e76b7689))


## v1.2.11 (2023-08-30)

### Fix

* fix: Update default config file path ([`436d55b`](https://github.com/timmyb824/python-SysInformer/commit/436d55b5fb1936c90cc32f50cb958ce224d41ca5))

### Unknown

* Merge pull request #47 from timmyb824/fix/default-config-path ([`4c0b8c8`](https://github.com/timmyb824/python-SysInformer/commit/4c0b8c882c4b6e7f02a64f669bcc62af0e07d265))


## v1.2.10 (2023-08-30)

### Chore

* chore(ci): update dist_exists value ([`19c9619`](https://github.com/timmyb824/python-SysInformer/commit/19c9619a1820cb21c8cf49223555ee38245e5212))

* chore(ci): add dist folder check before publishing ([`5fb6479`](https://github.com/timmyb824/python-SysInformer/commit/5fb6479e95402c749e509b9498189371817a088c))

* chore(ci): remove unnecessary if conditions ([`50f6945`](https://github.com/timmyb824/python-SysInformer/commit/50f6945ad3e7deea4f7e5d463cc13bcecdd5ad8c))

* chore(ci): add semantic release exit code echo ([`8cc4308`](https://github.com/timmyb824/python-SysInformer/commit/8cc43085aea1a59435bc10540ba889997f2c78db))

* chore(ci): remove unused Python Semantic Release step ([`2c8cb91`](https://github.com/timmyb824/python-SysInformer/commit/2c8cb91d3bfbd39170ce3797a6cd17ce618410a3))

### Documentation

* docs: Remove unnecessary information from README and config.yaml ([`25fde9f`](https://github.com/timmyb824/python-SysInformer/commit/25fde9f1773aaecd95683766932c3b8c74611a7c))

### Unknown

* Merge pull request #46 from timmyb824/ci/fix-ci-versioning10 ([`9ae083b`](https://github.com/timmyb824/python-SysInformer/commit/9ae083b439f0d270fe597d6731437bf6cec689b5))

* Merge pull request #45 from timmyb824/ci/fix-ci-versioning9 ([`de7c0a1`](https://github.com/timmyb824/python-SysInformer/commit/de7c0a1cf0a5d7ad55a7b0259fd6388272323069))

* Merge pull request #44 from timmyb824/ci/fix-ci-versioning8 ([`66b23ee`](https://github.com/timmyb824/python-SysInformer/commit/66b23eefcac44b470216daa4464bfe7384483d12))

* Merge pull request #43 from timmyb824/ci/fix-ci-versioning7 ([`64399c6`](https://github.com/timmyb824/python-SysInformer/commit/64399c6fa49c48ebd08c5c9d0ca46853169a6cc8))

* Merge pull request #42 from timmyb824/ci/fix-ci-versioning6 ([`73ba93c`](https://github.com/timmyb824/python-SysInformer/commit/73ba93c8dd94e2f3d24b4ee90d6c5c33a32edc69))


## v1.2.9 (2023-08-29)

### Ci

* ci: update ci.yaml script to test publish of new version ([`680d953`](https://github.com/timmyb824/python-SysInformer/commit/680d953c49a5233cb68162f29004447797f3fdef))

### Unknown

* Merge pull request #41 from timmyb824/ci/fix-ci-versioning5 ([`3eeee3a`](https://github.com/timmyb824/python-SysInformer/commit/3eeee3ae09cad095a557a49590aa8dfa2ffb36ae))


## v1.2.8 (2023-08-29)

### Ci

* ci: add error handling to version command as well ([`b8e8a7a`](https://github.com/timmyb824/python-SysInformer/commit/b8e8a7a72ed7bda2d484a5f5effd9bb1d88fc086))

### Unknown

* Merge pull request #40 from timmyb824/ci/fix-ci-versioning4 ([`8b3189d`](https://github.com/timmyb824/python-SysInformer/commit/8b3189d5171bdab9534bc3423696b970fbad7e79))


## v1.2.7 (2023-08-29)

### Chore

* chore(ci): optimize semantic-release workflow ([`12df791`](https://github.com/timmyb824/python-SysInformer/commit/12df7912b81cc323aa88089ddf6d9eb2e9b19195))

* chore: test no release attempt 2 ([`6870512`](https://github.com/timmyb824/python-SysInformer/commit/687051244231eb3ba5df22a9027f1f4cdeae14a1))

* chore: test no release ([`4d00623`](https://github.com/timmyb824/python-SysInformer/commit/4d006231b980681a66eca41259a389111d05a411))

* chore: fix extra ) ([`5546de2`](https://github.com/timmyb824/python-SysInformer/commit/5546de22e7e301240397c1f5800acd7b6cd94f16))

* chore: change publish to version ([`ba072df`](https://github.com/timmyb824/python-SysInformer/commit/ba072df0261b6e249425fa1018bcc774a59aa75e))

* chore: change publish to changelog -n ([`4e7ab9c`](https://github.com/timmyb824/python-SysInformer/commit/4e7ab9cfc6df80729ca1aaaded8a5766a79c8b53))

* chore: remove check for specific commit message prefixes and add check for publish output to determine if a new version is available before continuing with publishing and testing steps ([`7b802a9`](https://github.com/timmyb824/python-SysInformer/commit/7b802a90e900ff3f0fc839e99abf7e704d8f23c6))

* chore: add missing COMMIT_MSG variable ([`ca32b08`](https://github.com/timmyb824/python-SysInformer/commit/ca32b0827fedbc1f80f7d2303b61967b943e3d27))

* chore: fix initial step logic ([`62b6dc8`](https://github.com/timmyb824/python-SysInformer/commit/62b6dc8b9dd53d2a33895406595ca5f3437bbf3a))

* chore: add step to check prefixes ([`caa119b`](https://github.com/timmyb824/python-SysInformer/commit/caa119b00c11161828d96c5acec9c5429c94df43))

* chore: try checking env with shell script ([`a73b650`](https://github.com/timmyb824/python-SysInformer/commit/a73b6504b236e8c685eb7f02608a48616eb257df))

* chore: fix syntax error in if and use GITHUB_OUTPUT instead of GITHUB_ENV ([`4eaed2d`](https://github.com/timmyb824/python-SysInformer/commit/4eaed2d20015fe880cc4067ceb7fe3bf534fab09))

* chore: fix syntax error in if condition to correctly reference environment variable VERSION_OUTPUT ([`e6b8b29`](https://github.com/timmyb824/python-SysInformer/commit/e6b8b29918b762de6ac192a8d8029405d67a72fc))

* chore: try github_env in if logic ([`572f1e2`](https://github.com/timmyb824/python-SysInformer/commit/572f1e2c49cb52a76f5546f71b06bc27e421b143))

### Fix

* fix: Fix encoding issue in reading &#39;/proc/meminfo&#39; file ([`6ca10d2`](https://github.com/timmyb824/python-SysInformer/commit/6ca10d2134394b8b870d8bd64d45d511c24ea54e))

### Unknown

* Merge pull request #39 from timmyb824/ci/fix-ci-versioning3 ([`41a3f89`](https://github.com/timmyb824/python-SysInformer/commit/41a3f89381a16566c4d5a9cd3bce93b26306f888))

* Merge pull request #38 from timmyb824/ci/fix-ci-versioning2 ([`9512ec8`](https://github.com/timmyb824/python-SysInformer/commit/9512ec85ee352596e663976a85bc34fefdb9abdf))

* Merge pull request #37 from timmyb824/ci/fix-ci-versioning ([`2359e4e`](https://github.com/timmyb824/python-SysInformer/commit/2359e4ed7b5b6e3f86072d1dfcd00c0549b34e36))

* Merge pull request #36 from timmyb824/ci/test-ci ([`dede18a`](https://github.com/timmyb824/python-SysInformer/commit/dede18adaf160a75e32ce2c4bc528df0dd142b07))

* Merge pull request #35 from timmyb824/ci/ci-add-conditional13 ([`ec9aaba`](https://github.com/timmyb824/python-SysInformer/commit/ec9aabae8e94bc3f6a63a576164bd8da17cc5d9e))

* Merge pull request #34 from timmyb824/ci/ci-add-conditional12 ([`d17c56b`](https://github.com/timmyb824/python-SysInformer/commit/d17c56b97552d34ded21215821f35fe34a6b7c6d))

* Merge pull request #33 from timmyb824/ci/ci-add-conditional11 ([`c3fbfda`](https://github.com/timmyb824/python-SysInformer/commit/c3fbfda8f60002cb7255b33390872bcd6761d714))

* Merge pull request #32 from timmyb824/ci/ci-add-conditional10 ([`0c4223d`](https://github.com/timmyb824/python-SysInformer/commit/0c4223dab9864d1a184ab1c4844c3300daf800d2))

* Merge pull request #31 from timmyb824/chore/ci-add-conditional9 ([`f4501d2`](https://github.com/timmyb824/python-SysInformer/commit/f4501d2ffff9eab9ba9ab00a9c56c071691a89ae))

* Merge pull request #30 from timmyb824/chore/ci-add-conditional7 ([`eeb065e`](https://github.com/timmyb824/python-SysInformer/commit/eeb065e324f6629bec5ba5cbff90419d55b46733))

* Merge pull request #29 from timmyb824/ci/ci-add-conditional6 ([`1104c68`](https://github.com/timmyb824/python-SysInformer/commit/1104c68b59a4ab610666a950c94788623f12ba54))

* Merge pull request #28 from timmyb824/ci/ci-add-conditional5 ([`36c8aae`](https://github.com/timmyb824/python-SysInformer/commit/36c8aae027ddc3bf763ca7b36bb7e9fd0f95b737))

* Merge pull request #27 from timmyb824/ci/ci-add-conditional4 ([`29721d0`](https://github.com/timmyb824/python-SysInformer/commit/29721d065397f1a0dce2c615738f38770e9a1ff5))

* Merge pull request #26 from timmyb824/ci/ci-add-conditional3 ([`f6b0864`](https://github.com/timmyb824/python-SysInformer/commit/f6b0864e315bccb8c5268c4b6a303a0f3759d839))

* Merge pull request #25 from timmyb824/ci/ci-add-conditional2 ([`4c3eb66`](https://github.com/timmyb824/python-SysInformer/commit/4c3eb664a743455eba35c640ab9ef5d060a62850))


## v1.2.6 (2023-08-22)

### Chore

* chore: update makefile ([`4c29052`](https://github.com/timmyb824/python-SysInformer/commit/4c29052c84372ab2e2e2644b5c8998b667c0312d))

### Ci

* ci: update ci.yaml to add conditional logic ([`2b6c32a`](https://github.com/timmyb824/python-SysInformer/commit/2b6c32a2aa6b8b755c1bdd301c76d14ed61846ba))

### Unknown

* Merge pull request #24 from timmyb824/ci/ci-add-conditional ([`e89e6e0`](https://github.com/timmyb824/python-SysInformer/commit/e89e6e0907cc03b1b5034de616bb1f8c7a371b0c))

* Merge pull request #23 from timmyb824/chore/test-no-new-version ([`a4379ad`](https://github.com/timmyb824/python-SysInformer/commit/a4379ad20af5499de8dd3bc0d5b5cfee62bd379c))


## v1.2.5 (2023-08-21)

### Ci

* ci: update ci.yaml by removing outputs  and pyproject.toml by changing remove_dist config ([`72d3c4f`](https://github.com/timmyb824/python-SysInformer/commit/72d3c4f9aeb74d3378ed098c6b91cf9d30314e74))

### Unknown

* Merge pull request #22 from timmyb824/ci/fix-ci-again ([`a938963`](https://github.com/timmyb824/python-SysInformer/commit/a9389633e8fde8e80d4fa2b66be531c04b3bc15f))


## v1.2.4 (2023-08-21)

### Ci

* ci: update release step in ci.yaml ([`ac51e3d`](https://github.com/timmyb824/python-SysInformer/commit/ac51e3de03f4a2c9f148db168e73f39ec9b854af))

### Unknown

* Merge pull request #21 from timmyb824/ci/update-ci ([`26a1204`](https://github.com/timmyb824/python-SysInformer/commit/26a12040b05e5afa8e4c11fffb946bfbd308a673))


## v1.2.3 (2023-08-21)

### Ci

* ci: correct prepare package for release output ([`a0f3957`](https://github.com/timmyb824/python-SysInformer/commit/a0f395772b91ce7499cec71d513528035eacf169))

### Unknown

* Merge pull request #20 from timmyb824/ci/ci-ouput-tweaks ([`d0c341c`](https://github.com/timmyb824/python-SysInformer/commit/d0c341c36b0d2ec3dc8da867907f3906c78bb734))


## v1.2.2 (2023-08-21)

### Chore

* chore(changelog): remove old releases which had version discrepancies ([`45438f9`](https://github.com/timmyb824/python-SysInformer/commit/45438f99623c70b9a8aeeacfec97aee6ff6f6ac4))

### Ci

* ci: add conditional check to ci and update patch tags ([`f8cf1be`](https://github.com/timmyb824/python-SysInformer/commit/f8cf1be5da9ed7f393fb7a0f71ba83655f67eb31))

### Refactor

* refactor(ci): convert to trusted publisher ([`e1a2a78`](https://github.com/timmyb824/python-SysInformer/commit/e1a2a78e89b15c2c35a577a786765c92297cc456))

### Unknown

* Merge pull request #19 from timmyb824/ci/refactor-release-job ([`ea76682`](https://github.com/timmyb824/python-SysInformer/commit/ea76682b674f51c27a7160a9fda4b9434df18136))

* Merge pull request #18 from timmyb824/ci/trusted-publishing ([`b11dcc0`](https://github.com/timmyb824/python-SysInformer/commit/b11dcc0ecc1a305ab775b4d8b69cb0182b89c591))

* Merge pull request #17 from timmyb824/ci/cleanup-changelog ([`3e5ec68`](https://github.com/timmyb824/python-SysInformer/commit/3e5ec68e48de302aec0cae014eafddfabfc954e9))


## v1.2.1 (2023-08-21)

### Build

* build: Rename CI workflow and update dependencies ([`4ebd6a4`](https://github.com/timmyb824/python-SysInformer/commit/4ebd6a41a5ed5a8212bb061203cad4b829c8616c))

* build: Add fetch-depth and tags options in Checkout step ([`494b354`](https://github.com/timmyb824/python-SysInformer/commit/494b3544ef11d652261b1cf831882f1b4fbbce4d))

### Chore

* chore(ci): Update CI pipeline for package release ([`7b52af6`](https://github.com/timmyb824/python-SysInformer/commit/7b52af69ff805a98ca5f2854ce090e9fa72603db))

* chore: Update pyproject.toml build command ([`0c17c08`](https://github.com/timmyb824/python-SysInformer/commit/0c17c08fd0c6db5fe068a616e11f1dc25eeff14b))

* chore: Update version to 1.1.0 ([`2f7e9cc`](https://github.com/timmyb824/python-SysInformer/commit/2f7e9cc439cdccc89c06e49d5aa22a98dc735320))

* chore: empty changelog ([`a689080`](https://github.com/timmyb824/python-SysInformer/commit/a689080d3347902f0c3300cd721c6e665a46fe04))

* chore: Update default config path ([`1290b7d`](https://github.com/timmyb824/python-SysInformer/commit/1290b7d999e76b210bd4b822cadd2f2796243769))

* chore(ci): Disable CI workflow ([`111ce83`](https://github.com/timmyb824/python-SysInformer/commit/111ce83d2b81a6ccd379d54450eeb60e45cd26a8))

* chore(ci): remove unnecessary tags option ([`28bd83b`](https://github.com/timmyb824/python-SysInformer/commit/28bd83bc7f23d63b7be715466c5bdc8c39ab13ba))

* chore: update project version to 1.0.2 ([`e5ff9a2`](https://github.com/timmyb824/python-SysInformer/commit/e5ff9a201855409aadba65ea47db3a25b8f5454f))

* chore(ci): update GH_TOKEN in Prepare package for release ([`6904024`](https://github.com/timmyb824/python-SysInformer/commit/6904024f5f3b0250ebda93031fe7d05807222d06))

* chore(ci): Add test installation step ([`4dac46f`](https://github.com/timmyb824/python-SysInformer/commit/4dac46fccaced6dbefd6eebcda2c490f20ddde9c))

* chore: update remove_dist setting to true ([`a7ba0ad`](https://github.com/timmyb824/python-SysInformer/commit/a7ba0adae48921fcb80e49165ca94923938da744))

* chore: remove old dists ([`2526643`](https://github.com/timmyb824/python-SysInformer/commit/252664318e2a8bbd70fe610c06829945cd1e09ca))

* chore(ci): fix GH_TOKEN secret name ([`ec32430`](https://github.com/timmyb824/python-SysInformer/commit/ec32430eb3f3b35f423da9671218365e96407fe5))

* chore: Update version to 1.0.1 and add release job ([`c693e38`](https://github.com/timmyb824/python-SysInformer/commit/c693e38ff3b1dd21277c064f04e689f704d4bd58))

* chore(src): organized files into folders within src ([`6bf6c36`](https://github.com/timmyb824/python-SysInformer/commit/6bf6c3619be30340ee6e17c126c4b7ae61ed1e5d))

* chore(poetry): add doit package and other version bumps ([`07c2dc3`](https://github.com/timmyb824/python-SysInformer/commit/07c2dc3b3aebb654012bef1db96f9eb771bd4254))

* chore(tests): update import paths to account for new src folder structure ([`1888ec4`](https://github.com/timmyb824/python-SysInformer/commit/1888ec447d4d5837651b339dcb4a78608f92951c))

* chore: add distribution files for pez_servermonitor-1.0.0

feat(pyproject.toml): add pip-tools and pyinstaller as dependencies for tooling ([`cc52767`](https://github.com/timmyb824/python-SysInformer/commit/cc52767637e13597f8d7a78614842d75e34d4ed4))

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
fix(services.py): change exception variable name to exception in check_a_service function ([`e002556`](https://github.com/timmyb824/python-SysInformer/commit/e002556ab5ccf55a5accd1c42d6039036846913b))

* chore(config.yaml): remove unused services from config.yaml file

chore(pyproject.toml): remove commented out code and unused classifiers from pyproject.toml file

chore(main.py): remove redundant comments and unused import statements in main.py file
feat(main.py): refactor main function to improve code readability and maintainability ([`7d32610`](https://github.com/timmyb824/python-SysInformer/commit/7d32610b587a6cc01e6c118b662ea64a42582430))

* chore(.pre-commit-config.yaml): add hooks for poetry-check, poetry-lock, and poetry-export from poetry 1.5.0
chore(.pre-commit-config.yaml): add arguments to poetry-export hook to generate requirements.txt file
chore(requirements.txt): update hashes for distro, netifaces, ping3, psutil, pyyaml, and tabulate packages for Python 3.11 compatibility ([`eff478a`](https://github.com/timmyb824/python-SysInformer/commit/eff478a911b08ac18e08afbba9f2d242cf68ce01))

* chore: Update Python version to 3.11.2 ([`e163c70`](https://github.com/timmyb824/python-SysInformer/commit/e163c707244dd18489db3046c6bc116d9290375e))

* chore: Update dependencies and requirements ([`eea9fdc`](https://github.com/timmyb824/python-SysInformer/commit/eea9fdcfcc6e9a875ce3b1affa11de2a6d437235))

* chore: update poetry version to 1.5.1 ([`ba68502`](https://github.com/timmyb824/python-SysInformer/commit/ba68502ce367e85d72f34c44b77c14a9c6f6d70c))

* chore: update build-test.yaml ([`7b934e0`](https://github.com/timmyb824/python-SysInformer/commit/7b934e0d039406dbcb9a81f9557149d5ef03c9fd))

* chore: Update command in build-test.yaml ([`ad2a050`](https://github.com/timmyb824/python-SysInformer/commit/ad2a050ae2d20a4156b717c063d79a841a170f00))

* chore: Update build-test.yaml ([`1d90930`](https://github.com/timmyb824/python-SysInformer/commit/1d9093084697e7457761da58bd6ee24c9294782a))

* chore: update build-test.yaml ([`3040bfe`](https://github.com/timmyb824/python-SysInformer/commit/3040bfeee61b78e1fa3f2ea72dc41d17e61bea46))

* chore: streamline script execution in workflow ([`a24d632`](https://github.com/timmyb824/python-SysInformer/commit/a24d632c6eda07eef95eed5134b03b75940f61fe))

* chore: Add environment variable for production environment ([`57973cf`](https://github.com/timmyb824/python-SysInformer/commit/57973cfcc09d0cfaf2f5a8741925fd886c1cec88))

* chore(ci): Remove unnecessary docker container check ([`213a78b`](https://github.com/timmyb824/python-SysInformer/commit/213a78bf210ed7fb0203a0ed0c93aac9d896c238))

* chore: Remove unnecessary ping hosts and add docker test cmd ([`2388483`](https://github.com/timmyb824/python-SysInformer/commit/238848335c054da4273196ade92ba5ebfc0c14a3))

* chore(build-test.yaml): update Python version to 3.10.12 ([`e0f5f89`](https://github.com/timmyb824/python-SysInformer/commit/e0f5f89fc2b6383239f296c20f48fc446d9fb274))

* chore: add ignore-pre-commit script ([`9a1bf52`](https://github.com/timmyb824/python-SysInformer/commit/9a1bf52d57cd0c7b482170822afbd8d5801148db))

### Ci

* ci: Run semantic-release for versioning and changelog ([`3156930`](https://github.com/timmyb824/python-SysInformer/commit/31569304e43ea8412a3aad99fd5d8f4cf99b4b26))

* ci: fix incorrect parameter name for repository-url ([`abc94c8`](https://github.com/timmyb824/python-SysInformer/commit/abc94c83e031c818e97e565d2d58707d3934e6c2))

* ci(build-test.yaml): update when workflow runs and correct final step ([`dcca906`](https://github.com/timmyb824/python-SysInformer/commit/dcca9060ea05140324e78333c8c49cdaa65adef6))

### Feature

* feat(ci): Replace semantic-release with its own github action ([`16fe398`](https://github.com/timmyb824/python-SysInformer/commit/16fe398e69cdb5fe5deee326228cd5abb0d6fa4d))

* feat: Update Dockerfile and docker-compose.yaml ([`a97b190`](https://github.com/timmyb824/python-SysInformer/commit/a97b19021444f7f14a03fb6b4d607cc47899f049))

* feat(ci): add CI workflow for testing and publishing the app with python semantic versioning ([`2e6949d`](https://github.com/timmyb824/python-SysInformer/commit/2e6949d655acaed19f0938d44d80b0e02bc66814))

* feat(main.py): convert arg parse to click library ([`7010c60`](https://github.com/timmyb824/python-SysInformer/commit/7010c60e280b94e23235caebc38ccfec416d49c9))

* feat(main.py): convert arg parse to click library ([`f46074a`](https://github.com/timmyb824/python-SysInformer/commit/f46074a19d1db5bbe61d0d7fda8b23a7838fe29f))

* feat: add build and test GitHub Actions workflow ([`7041694`](https://github.com/timmyb824/python-SysInformer/commit/704169429bcc45247a3ec29e66d53e644355e34a))

### Fix

* fix(pyproject): add correct version_toml and correct build command ([`74c5ad1`](https://github.com/timmyb824/python-SysInformer/commit/74c5ad188bc1c4642d694e0a2d0629f994b025ee))

* fix(main): Fix imports and function calls ([`74733f2`](https://github.com/timmyb824/python-SysInformer/commit/74733f2e09417a9f6930bc02e83bd5ef95a34c01))

* fix(test_latency.py): update expected result in test_check_ping to match the actual format of the returned value
fix(test_latency.py): update expected results in test_perform_ping to match the actual format of the returned values ([`1a23667`](https://github.com/timmyb824/python-SysInformer/commit/1a23667aecb5b2383acd4bd761d301cd20b0ffc4))

* fix: set pyproject back ([`b6b05cb`](https://github.com/timmyb824/python-SysInformer/commit/b6b05cb1d84db6c43c07339e096c96074ec79d7c))

* fix(cpu): properly handle missing cpu information ([`000c8cc`](https://github.com/timmyb824/python-SysInformer/commit/000c8cce37acbf03e2c2f78750bca67fd774f563))

### Refactor

* refactor: Update package name and config file path ([`81a7ba0`](https://github.com/timmyb824/python-SysInformer/commit/81a7ba003941cf8e6cf28f8fa0eba3f147a19bce))

* refactor(src): clean up exceptions and prints; set PYTHONPATH ([`64968c2`](https://github.com/timmyb824/python-SysInformer/commit/64968c298a4198d995c9b695e764d2a0c4d0993f))

* refactor: stop program from exiting; precommit updates ([`ab30096`](https://github.com/timmyb824/python-SysInformer/commit/ab30096f7f296f25b808c76262dc8397c1966568))

### Test

* test: test packages pattern in pyproject ([`f695a93`](https://github.com/timmyb824/python-SysInformer/commit/f695a93fc0aa46fa71da905e46e25ac60a41b1c0))

* test: add mock functions for cpu info ([`124d5d0`](https://github.com/timmyb824/python-SysInformer/commit/124d5d00f178317450177c0a1ccf79b2a4010156))

* test(test): add many tests, new configs, and other changes ([`01d3ec4`](https://github.com/timmyb824/python-SysInformer/commit/01d3ec4d4e4a458634af24eae11f2482c2313b5c))

* test(test_config_parser): adds tests for parse_config_file function ([`39bbd05`](https://github.com/timmyb824/python-SysInformer/commit/39bbd05f9245251fc6221bea9d5f71b8f4b716e2))

### Unknown

* Merge pull request #16 from timmyb824/ci/fix-poetry-semantic-build-issues ([`e6180ef`](https://github.com/timmyb824/python-SysInformer/commit/e6180ef7d521ee758f39db1a764a3d463d7fce5e))

* Merge pull request #15 from timmyb824/ci/switch-semantic-release-back-to-shell ([`1685abd`](https://github.com/timmyb824/python-SysInformer/commit/1685abde2db99fa6eb00afb0b94d4123b944d138))

* Merge pull request #14 from timmyb824/ci/fix-semantic-release-action ([`47bdc09`](https://github.com/timmyb824/python-SysInformer/commit/47bdc09c0be2836830b12fc1c54c65b91e4af0c4))

* Merge pull request #13 from timmyb824/ci/use-semantic-action ([`c43a04d`](https://github.com/timmyb824/python-SysInformer/commit/c43a04d7c3d975f87099fba44b229f0a140c43ff))

* Merge pull request #12 from timmyb824/ci/re-enable-ci ([`bcce789`](https://github.com/timmyb824/python-SysInformer/commit/bcce789f09e9dfd47f3330a4ad580269d9460772))

* Merge pull request #11 from timmyb824/feat/change-name ([`3cb973f`](https://github.com/timmyb824/python-SysInformer/commit/3cb973fe1e256174c4efaa26333b30a8b3d6d38c))

* Merge pull request #10 from timmyb824/ci/more-fixes ([`4207b59`](https://github.com/timmyb824/python-SysInformer/commit/4207b59d0e88a2daa3382c9e1470ea4da3848b1b))

* Merge pull request #9 from timmyb824/ci/fix-gh-token ([`7e58917`](https://github.com/timmyb824/python-SysInformer/commit/7e58917e845622eeca09f895678f752ae5219aaa))

* Merge pull request #8 from timmyb824/ci/repo-url ([`1bf42a5`](https://github.com/timmyb824/python-SysInformer/commit/1bf42a554dd950029cb30e8acc9e4abe984ecbab))

* Merge pull request #7 from timmyb824/ci/repo-url ([`4b3ef45`](https://github.com/timmyb824/python-SysInformer/commit/4b3ef4518401c92b408edc2bb852fdb1ae82d804))

* Merge pull request #6 from timmyb824/ci/fix-ci ([`f1cf491`](https://github.com/timmyb824/python-SysInformer/commit/f1cf491631a3737cf5a402d516762c6a0c5723a3))

* Merge pull request #5 from timmyb824/ci/fix-auto-versioning ([`35f5175`](https://github.com/timmyb824/python-SysInformer/commit/35f51759c5a4e257cef6160b25e8653a03aafa19))

* Merge pull request #4 from timmyb824/automate-versioning ([`dc3ddfa`](https://github.com/timmyb824/python-SysInformer/commit/dc3ddfae0016aac7f0dc2d312891a0d5f4d8ea2b))

* Merge pull request #3 from timmyb824:click

chore(tests): update import paths to account for new src folder struc… ([`3195740`](https://github.com/timmyb824/python-SysInformer/commit/31957404f9e7eff670bdc4986c1d89b92d9b94cc))

* Update README.md ([`f5afcb6`](https://github.com/timmyb824/python-SysInformer/commit/f5afcb6b04ad89dabc72d662ab66563bef4fddde))

* update(readme.md): add new gif ([`2422b63`](https://github.com/timmyb824/python-SysInformer/commit/2422b6380b476a096ebd28a7f8f2d8e41cd62bc5))

* Update README.md ([`898d83f`](https://github.com/timmyb824/python-SysInformer/commit/898d83f3477f5b256d1c1a6d1a4da7d010a05f12))

* update(main): fix latency test; update readme; add gif ([`27f6991`](https://github.com/timmyb824/python-SysInformer/commit/27f69914fc2b7bc5b2475ebc2543c26c583908ff))

* Create LICENSE ([`2615c77`](https://github.com/timmyb824/python-SysInformer/commit/2615c773e51e1de2d7b54ebf94fa2f8531a0a4dd))

* Merge pull request #2 from timmyb824/dockerize ([`3f17433`](https://github.com/timmyb824/python-SysInformer/commit/3f174337a4aa7ef6bbb098c52c0b7fb4144698a1))

* update(dockerize): add docker files and return UNKNOWN values for CPU info upon IOError ([`089e49c`](https://github.com/timmyb824/python-SysInformer/commit/089e49cd3a1e24bde78ec3b8aebc04ba59647195))

* Merge pull request #1 from timmyb824/improvements_v1 ([`4449d1b`](https://github.com/timmyb824/python-SysInformer/commit/4449d1b25bc717c470e62af4ac1306c700e6451f))

* UPDATE(improvements_v1): add custom exceptions ([`4c91c25`](https://github.com/timmyb824/python-SysInformer/commit/4c91c25cfcd3ddbca2fa4f3e2328c35588dda5ec))

* UPDATE(improvements_v1): add top processes by cpu mem ([`632a776`](https://github.com/timmyb824/python-SysInformer/commit/632a7764466d526217d9f10da46ce131f1b2131d))

* UPDATE(improvements_v1): move config file to args ([`5671fb7`](https://github.com/timmyb824/python-SysInformer/commit/5671fb73964a0cd08940c96d9a62d7718134e791))

* UPDATE(improvements_v1): refactor to add error handling, docstrings, and other improvements ([`808a5c2`](https://github.com/timmyb824/python-SysInformer/commit/808a5c29810ce7ea01aa8d553816879be3c50610))

* UPDATE(improvements_v1): add started readme ([`3283830`](https://github.com/timmyb824/python-SysInformer/commit/3283830156ca0fde900b960bcbbace09bbf5a4a1))

* init commit ([`edb8783`](https://github.com/timmyb824/python-SysInformer/commit/edb8783b53a4c1d2569b64ad49b38097637fd930))
