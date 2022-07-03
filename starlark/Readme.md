Reference link:

https://docs.bazel.build/versions/main/skylark/rules-tutorial.html

ctx:
1. A context object that is passed to the implement function for a rule or aspect. It provides access to the information and methods needed to analyze the current target.
1. It lets the implementation function access the current target's label, attributes, configuration, and the providers of its dependencies.
1. It has methods for declaring output files and the actions that produce them.