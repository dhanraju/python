# Build rules for mocking examples.

py_binary(
    name = "calculator_app",
    srcs = ["calculator.py",],
    main = "calculator.py",
)

py_test(
    name = "calculator_test",
    srcs = ["calculator_test.py",],
    deps = [":calculator_app"],
)

py_test(
    name = "calculator_using_mock_test",
    srcs = ["calculator_using_mock_test.py",],
    deps = [":calculator_app"],
)

py_binary(
    name = "create_tar",
    srcs = ["create_tar.py",],
    main = "create_tar.py",
)

py_test(
    name = "create_tar_mock_test",
    srcs = ["create_tar_mock_test.py",],
    deps = [":create_tar"],
)
