# Default Docx Template

Template for docx myst exports

![](thumbnail.png)

- Author: Franklin Koch (executablebooks)
- Author Website: https://github.com/executablebooks/mystjs
- [Submission Guidelines](https://github.com/executablebooks/mystjs)

## Steps to creating your own template!

- [x] 🆕 Create this repository. Nailed it. 🚀
- [ ] 📑 Replace the `template.tex` with your existing LaTeX template/article
- [ ] 👯‍♀️ Copy in any other style, definitions or images necessary for the template
- [ ] 👩‍🔬 Add the files necessary into `files` list in the `template.yml` ([documentation](https://js.myst.tools/jtex/template-yml))
- [ ] 🧙‍♀️ Start replacing template values with `[-options.my_value-]` and put in `[# if parts.abstract #]` conditions to toggle sections on and off ([documentation](https://js.myst.tools/jtex/template-rules))
- [ ] 👩🏿‍💻 Install [jtex](https://js.myst.tools/jtex) (`npm install -g jtex`) and run `jtex check` ([documentation](https://js.myst.tools/jtex/command-line))
- [ ] 🪄 Continue to improve the options in your template for `parts` and `options` ([documentation](https://js.myst.tools/jtex/document))
- [ ] 💾 When ready, save your `template.yml` and run `jtex check --fix`, this will add various packages that are auto detected and fix document options ([documentation](https://js.myst.tools/jtex/command-line))
- [ ] 🧪 Test with real content: `myst build my-document.md --template ../path/to/template` ([documentation](https://js.myst.tools/guide/creating-pdf-documents))
- [ ] 📸 Create a `thumbnail.png` with an accurate screenshot of the template
- [ ] 🧭 Update this README, and check all values in the `template.yml`
- [ ] 🚀 Push to GitHub, and contribute to the [community templates repository](https://github.com/myst-templates/templates)
