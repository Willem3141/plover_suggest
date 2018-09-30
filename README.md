A plugin for Plover that allows you to see suggestions without having the suggestions window open.

To use it, define a stroke like

```
    "STKPW": "{PLOVER:SUGGEST}",
```

and press it to see a system notification with suggestions pop up.

[A screenshot of the plugin in action](https://wimiso.nl/random/plover-suggest.png)

This is hacky and depends on `notify-send` being available, so this will work on GNU/Linux systems only.
