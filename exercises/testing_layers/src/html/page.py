def page(content):
    """Generate the main HTML page structure."""
    content_html = "".join(content)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skiller Wordle</title>
    <style>{"""
        * {
            box-sizing: border-box;
            margin: 0;
        }

        body {
            font-family: Arial, sans-serif;
            font-size: 16px;
            width: 19rem;
            margin: 0 auto;
            padding: 1rem;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        h1, p {
            text-align: center;
            margin: 0;
        }

        form {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }

        input {
            width: 100%;
            padding: 0.5rem;
            border: 2px solid #ccc;
            text-align: center;
            text-transform: uppercase;
            font-size: 1.5rem;
        }

        .error {
            background-color: lightcoral;
            color: white;
            font-weight: bold;
            width: 100%;
            padding: 0.5rem;
            text-align: center;
        }

        .guesses {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }

        .guess {
            display: flex;
            gap: 0.5rem;

            span {
                display: flex;
                font-size: 1.5rem;
                width: 3rem;
                height: 3rem;
                line-height: 1;
                justify-content: center;
                align-items: center;
                border: 2px solid #ccc;
                text-transform: uppercase;
                font-weight: bold;
            }
        }

        .gray, .yellow, .green {
            color: white;
            border: none;
        }

        .gray {
            background-color: #787c7a;
        }

        .yellow {
            background-color: #c9b458;
        }

        .green {
            background-color: #6aaa64;
        }

        .correct-answer {
            font-weight: bold;
            text-transform: uppercase;
        }
    """}</style>
</head>
<body>
    <h1>Skiller Wordle</h1>
    {content_html}
</body>
</html>"""
