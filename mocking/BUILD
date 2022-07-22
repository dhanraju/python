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