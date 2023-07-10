#!/usr/bin/env bats

@test "Test success" {
    run pwd
    [ "$status" -eq 0 ]
}

# @test "Test failure" {
#     run ls
#     [ "$status" -eq 0 ]
#     [ "${lines[0]}" = "unknown" ]
# }
