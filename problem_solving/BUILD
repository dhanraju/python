py_binary(
    name = "sum_of_three_ints",
    srcs = ["sum_of_three_ints.py",],
    main = "sum_of_three_ints.py",
)

py_test(
    name = "sum_of_three_ints_test",
    srcs = [":sum_of_three_ints_test.py",],
    deps = [":sum_of_three_ints"]
)