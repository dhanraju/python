def _foo_binary_impl(ctx):
    print("analyzing", ctx.label)
    print("actions", ctx.actions)
    # print("aspect_ids", ctx.aspect_ids)
    print("attr", ctx.attr)
    print("bin_dir", ctx.bin_dir)
    print("build_file_path", ctx.build_file_path)
    # print("build_setting_value", ctx.build_setting_value)
    print("configuration", ctx.configuration)
    print("coverage_instrumented()", ctx.coverage_instrumented(target=None))
    print("created_actions()", ctx.created_actions())
    print("default_provider", ctx.default_provider)
    print("disabled_features", ctx.disabled_features)
    print("exec_groups", ctx.exec_groups)
    print("file", ctx.file)
    print("files", ctx.files)
    print("fragments", ctx.fragments)
    print("genfiles_dir", ctx.genfiles_dir)
    print("host_configuration", ctx.host_configuration)
    print("host_fragments", ctx.host_fragments)
    print("label", ctx.label)
    print("outputs", ctx.outputs)
    print("resolve_tools(tools=[])", ctx.resolve_tools(tools=[]))
    # print("rule", ctx.rule)
    print("split_attr", ctx.split_attr)
    print("toolchains", ctx.toolchains)
    print("var", ctx.var)
    print("workspace_name", ctx.workspace_name)

    # Creating a file
    out = ctx.actions.declare_file(ctx.label.name)
    ctx.actions.write(
        output = out,
        content = "Hello\n",
    )
    return [DefaultInfo(files = depset([out]))]

foo_binary = rule(
    implementation = _foo_binary_impl,
)

print("bzl file evaluation")