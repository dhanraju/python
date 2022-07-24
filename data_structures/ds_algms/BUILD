py_binary(
    name = "ch01_exercises",
    srcs = ["ch01_exercises.py"],
    main = "ch01_exercises.py",
)

py_test(
    name = "ch01_exercises_test",
    srcs = ["ch01_exercises_test.py",],
    deps = [":ch01_exercises",],
)

# Not working
# py_test(
#    name = "ch01_exercises_gtest_test",
#    srcs = ["ch01_exercises_gtest_test.py",],
#    deps = [":ch01_exercises",],
# )

py_binary(
    name = "ch02_oops_credit_card",
    srcs = ["ch02_oops_credit_card.py",],
    main = "ch02_oops_credit_card.py",
)

py_test(
    name = "ch02_oops_credit_card_test",
    srcs = ["ch02_oops_credit_card_test.py",],
    deps = [":ch02_oops_credit_card",],
)

py_binary(
    name = "ch02_op_overlo_vector",
    srcs = ["ch02_op_overlo_vector.py",],
    main = "ch02_op_overlo_vector.py",
)

py_test(
    name = "ch02_op_overlo_vector_test",
    srcs = ["ch02_op_overlo_vector_test.py",],
    deps = [":ch02_op_overlo_vector",],
)

py_binary(
    name = "ch02_op_overlo_iterators",
    srcs = ["ch02_op_overlo_iterators.py",],
    main = "ch02_op_overlo_iterators.py",
)

py_test(
    name = "ch02_op_overlo_iterators_test",
    srcs = ["ch02_op_overlo_iterators_test.py",],
    deps = [":ch02_op_overlo_iterators",],
)

py_binary(
    name = "ch02_op_overlo_range",
    srcs = ["ch02_op_overlo_range.py",],
    main = "ch02_op_overlo_range.py",
)

py_test(
    name = "ch02_op_overlo_range_test",
    srcs = ["ch02_op_overlo_range_test.py",],
    deps = [":ch02_op_overlo_range",],
)

py_binary(
    name = "ch02_op_inherit_credit_card",
    srcs = ["ch02_op_inherit_credit_card.py",],
    main = "ch02_op_inherit_credit_card.py",
    deps = [":ch02_oops_credit_card"],
)

# py_test(
#    name = "ch02_op_inherit_credit_card_test",
#    srcs = ["ch02_op_inherit_credit_card_test.py",],
#    deps = [":ch02_op_inherit_credit_card",],
# )

py_binary(
    name = "ch02_op_inherit_progression",
    srcs = ["ch02_op_inherit_progression.py",],
    main = "ch02_op_inherit_progression.py",
)

py_binary(
    name = "ch02_op_inherit_arith_prog",
    srcs = ["ch02_op_inherit_arith_prog.py",],
    main = "ch02_op_inherit_arith_prog.py",
    deps = [":ch02_op_inherit_progression",],
)

py_binary(
    name = "ch02_op_inherit_geom_prog",
    srcs = ["ch02_op_inherit_geom_prog.py",],
    main = "ch02_op_inherit_geom_prog.py",
    deps = [":ch02_op_inherit_progression",],
)

py_binary(
    name = "ch02_op_inherit_fibo_prog",
    srcs = ["ch02_op_inherit_fibo_prog.py",],
    main = "ch02_op_inherit_fibo_prog.py",
    deps = [":ch02_op_inherit_progression",],
)
