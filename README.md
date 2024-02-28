<div align="center">

  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="Prymal.png">
    <img alt="Ktor logo" src="Prymal.png">
  </picture>

  [![Status](https://img.shields.io/badge/Status-In_Development-red)](/../../)
  [![Versions](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FJustinBacher%2FPrymal%2Fmain%2Fpyproject.toml&logo=python&labelColor=yellow)](https://python.org/)
  [![License](https://img.shields.io/github/license/JustinBacher/Prymal?color=blue)](LICENSE.txt)
  [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
  [![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
</div>

> ⚠️ This document is currently in draft form! It will be updated substantially as Prymal is being developed.
> Principles explained in this document may not make it to the end product, that said this outlines the core aim of the project.

# What is Prymal? 🤷

Prymal is a groundbreaking UI framework designed to revolutionize frontend development by providing an abstract and versatile approach to building user interfaces.
Inspired by the best aspects of frameworks such React, React Native, Svelte, and Qwik Prymal aims to simplify and modernize the current UI development process.

## Write once deliver everywhere 🚀

Prymal allows you to create your UI components once and effortlessly deploy them across various platforms, including web, iOS, Android, and desktop.
This ensures a consistent user experience across different devices, reducing development time and effort.

## Rich UI Abstraction 🍱

Inspired by React Native Prymal abstracts from typical UI elements.
For instance, it introduces concepts like `Container` as a substitute for the traditional `<div>`, and `Text` to replace `<span>`, `<p>` or textual `<div>` tags.
This not only aligns with modern UI development trends but also enhances code clarity and maintainability by introducing more semantic and expressive components.

## Styling made easy 🎨

No more convoluted style sheets or complex configurations.
Define a Style at creation or apply a Style directly to UI a element using the `@` operator.

Python:
```py
emphasis = font_decoration.underline & colors.red

example = Container(style=styles.flex_direction.horizontal)(
    Text("Hello World!") @ emphasis & font_weight.bold,
)
```

HTML:
```html
<div class="example">
  <p class="emphasis">Hello World!</p>
</div>

<style>
  .example {
    display: flex;
    flex-direction: row;
  }
  .emphasis {
    font-weight: bold;
    text-decoration: underline;
    color: red;
  }
</style>
```

Styles are seamlessly handled by Prymal in the background.
