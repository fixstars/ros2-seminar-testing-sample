# ROS2 Seminar - Testing Sample

本リポジトリは[ROS2自律走行実現に向けて～次世代ロボット開発フレームワークROS2のテストフレームワーク徹底理解～](https://speakerdeck.com/fixstars/autonomous-driving-realization-by-ros2-test-framework) セミナーで発表した事項のサンプルコードとなっている。

## Folders

- [one-by-one](./one-by-one/) : テストフレームワーク毎のサンプル。セミナー資料の "ROS2で可能なテスト/lint" のテストに対応。
- [lint](./lint/) : リントのサンプル。セミナー資料における "ROS2で可能なテスト/lint" の lint に対応。
- [sample](./sample/) : テスト実装を含むパッケージ開発のサンプル。セミナー資料における "サンプルアプリでのテスト実装" に対応。

デフォルトでは全てのテストがパスするようになっている。失敗するテストケースについてはコメントアウトされているため、挙動を確認したい時はコメントアウトを外す。

## Prerequisites

- ROS2 Humble (ros-humble-desktop)
- ros-humble-ament-cmake-google-benchmark
- ros-humble-launch-pytest
- bats (サンプルの1つで使用している)

## Setup

ROS2 Humble のセットアップは完了しているものとして、上記追加パッケージ及び mixin を導入する。mixin はパフォーマンステストを実行する時に使用する。

```shell
# 追加パッケージを導入
sudo apt install ros-humble-ament-cmake-google-benchmark ros-humble-launch-pytest bats

# mixin を導入
colcon mixin add default https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml
colcon mixin update
```

また、コマンド実行時に `SetuptoolsDeprecationWarning` 警告が出るため、必要に応じて以下の環境変数を設定して抑制する。

```shell
export PYTHONWARNINGS=ignore:::setuptools.command.install,ignore:::setuptools.command.easy_install
```

## Build

```shell
colcon build --symlink-install
```

## Test

```shell
# テスト結果を標準出力に表示させるために --event-handers オプションを追加。
colcon test --event-handlers console_direct+ 
```

## Benchmark

パフォーマンステストを実行する。セミナーでは解説していないが [Google Benchmark](https://github.com/google/benchmark) を使用したパフォーマンステストも可能で、 [one-by-one/06_example_ament_cmake_google_benchmark](./one-by-one/06_example_ament_cmake_google_benchmark/) にサンプルがある。

```shell
# リリースビルドを行うので別ディレクリを作成する
mkdir -p release

# リリースビルド。--mixin release により必要なオプションが設定される。
# パフォーマンステストのコードをビルドするために -DAMENT_RUN_PERFORMANCE_TESTS=ON を設定。
colcon --log-base release/log build --build-base release/build --install-base release/intall --ament-cmake-args -DAMENT_RUN_PERFORMANCE_TESTS=ON --mixin release --symlink-install

# パフォーマンステストを実行。並列実行では測定に影響が出るため、--executor sequential を指定する。
colcon --log-base release/log test --build-base release/build --install-base release/intall --event-handlers console_direct+ --ctest-args ' -L performance --no-tests=ignore' --executor sequential
```

## License

本プロジェクトは MIT License である。
