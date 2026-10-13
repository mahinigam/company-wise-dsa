# Contributing and local validation

Before adding or changing a solution:

1. Keep the problem summary in your own words and link the original exercise.
2. Include difficulty, topic, preparation tags, the key idea, and complexity.
3. Add executable assertions for ordinary and edge-case inputs.
4. Run the complete repository check:

```bash
python -m compileall -q problems tests
python tests/run_examples.py
```

The example runner executes every Python solution module. It uses only the Python standard library, so no third-party test framework is required.

Company labels are study guidance unless a trustworthy source explicitly verifies a problem/company association. Prefer focused changes, review the diff, and don't claim a solution is tested unless the commands above pass.
