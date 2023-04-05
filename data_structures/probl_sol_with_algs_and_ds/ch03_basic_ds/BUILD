# Stack Implementation and applications.
py_library(
    name = "stack_lib",
    srcs = ["stack.py",],
)

py_test(
    name = "stack_lib_test",
    srcs = ["stack_test.py",],
    deps = [":stack_lib",],
    main = "stack_test.py",
)

py_binary(
    name = "reversing_string",
    srcs = ["reversing_string.py",],
    main = "reversing_string.py",
)

py_binary(
    name = "paranthesis_checker",
    srcs = ["paranthesis_checker.py",],
    main = "paranthesis_checker.py",
)

py_binary(
    name = "base_converter",
    srcs = ["base_converter.py",],
    main = "base_converter.py",
)

py_binary(
    name = "infix_to_postfix",
    srcs = ["infix_to_postfix.py",],
    main = "infix_to_postfix.py",
)

py_binary(
    name = "postfix_evaluation",
    srcs = ["postfix_evaluation.py",],
    main = "postfix_evaluation.py",
)

# Queue Implementation and applications.
py_library(
    name = "queue_lib",
    srcs = ["queue.py",],
)

py_test(
    name = "queue_lib_test",
    srcs = ["queue_test.py",],
    deps = [":queue_lib",],
    main = "queue_test.py",
)

py_binary(
    name = "hot_potato_problem",
    srcs = ["hot_potato_problem.py",],
    deps = [":queue_lib",],
    main = "hot_potato_problem.py",
)

py_binary(
    name = "printing_tasks",
    srcs = ["printing_tasks.py",],
    deps = [":queue_lib",],
    main = "printing_tasks.py",
)
