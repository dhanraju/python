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

py_binary(
    name = "merge_overlap_intervals",
    srcs = ["merge_overlap_intervals.py",],
    main = "merge_overlap_intervals.py",
)

py_test(
    name = "merge_overlap_intervals_test",
    srcs = ["merge_overlap_intervals_test.py",],
    deps = [":merge_overlap_intervals"]
)