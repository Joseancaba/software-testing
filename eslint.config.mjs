import js from "@eslint/js";
import globals from "globals";

export default [
  js.configs.recommended,
  {
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "script",
      globals: globals.node, // habilita console, process, etc.
    },
    rules: {
      // tus reglas aquí si quieres
    },
  },
];
