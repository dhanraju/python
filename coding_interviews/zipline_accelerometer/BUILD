py_binary(
    name = "my_mcu_fwk",
    srcs = ["my_mcu_fwk.py"],
    main = "my_mcu_fwk.py"
)

py_test(
    name = "dut_test",
    srcs = ["dut_test.py"],
    deps = [":my_mcu_fwk"],
)