adb install some.apk

adb shell pm list packages -3

frida -U -f $pkg --codeshare fdciabdul/frida-multiple-bypass -l out/_agent.js

trace_puller.sh $pkg /out_dir/ 

python3 trace_cleaner.py ./out_dir/ ./out_dir/merged.trace



# Meeting Summary

After brainstorming and exploring various methods to integrate static analysis results with an LLM model to automatically explore application UIs and trigger target methods, we concluded that this approach currently seems infeasible due to limitations in understanding and implementation.

# Next Steps

- Conduct a more focused evaluation of AutoDroid, particularly on applications outside its training set, and analyze the results.
- Deepen knowledge in prompt engineering to facilitate the above evaluation.

## Potential Improvements for AutoDroid

- **Expand Actions**: Currently, AutoDroid is limited to clicking on UI elements. Exploring additional actions such as scrolling, swiping, or enabling/disabling network or Wi-Fi could enhance its capabilities.
- **Teach New Actions to LLM**: These expanded actions can be incorporated into the LLM's training to improve interaction possibilities.
- **Enrich Prompts**: Provide the LLM with additional information not currently available through AutoDroid, such as:
    - Screenshots of the application.
    - Or any other information that could be extracted for example with frida. the ui hierarchy and type of listeners.
- **Task Completion Limitations**: AutoDroid lacks the ability to confirm when a task within an application is complete, and there is no clear method to assess UI task completion.
- **Dataset Introduction**: To address this limitation, a new dataset could be developed. It would include:
  - Applications and their categories.
  - A map of tasks and their corresponding completion criteria.
  - This dataset could serve as a benchmark for evaluating the model's performance in task completion.
