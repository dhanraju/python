# load("@rules_proto//proto:defs.bzl", "proto_library")
# Fixed py_proto_library errors by following the step to import protobuf
# dependency in
# https://thethoughtfulkoala.com/posts/2020/05/08/py-protobuf-bazel.html
load("@com_google_protobuf//:protobuf.bzl", "py_proto_library")

package(default_visibility = ["//visibility:public"])

# proto_library(
#    name = "addressbook_proto",
#    srcs = ["addressbook.proto"],
# )

py_proto_library(
    name = "addressbook_py_pb2",
    srcs = ["addressbook.proto"],
    # deps = ["addressbook_proto"],
    # deps = ["@com_google_protobuf//:protobuf_python"],
)

py_binary(
    name = "addressbook",
    srcs = ["addressbook.py"],
    deps = ["addressbook_py_pb2"]
)

py_binary(
    name = "write_addressbook",  # Target name should be same as source file name.
    srcs = ["write_addressbook.py"],
    deps = ["addressbook_py_pb2"]
)

py_binary(
    name = "read_addressbook",
    srcs = ["read_addressbook.py"],
    deps = ["addressbook_py_pb2"]
)