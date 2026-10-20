# Databytes Streamlit Learning Labs

This starter project hosts three existing interactive HTML labs inside a Streamlit app.

## Files

- `app.py` — Streamlit navigation page
- `labs/overfitting.html`
- `labs/regularization.html`
- `labs/prompt_injection.html`
- `requirements.txt` — deployment dependency

## Test locally

Install Python, then run:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL printed in the terminal.

## Deploy publicly

1. Create a GitHub repository, for example `databytes-learning-labs`.
2. Upload `app.py`, `requirements.txt`, and the entire `labs` folder.
3. Open https://share.streamlit.io/ and sign in with GitHub.
4. Choose **Create app**, select the repository and branch, and set the main file to `app.py`.
5. Deploy. In the app's sharing settings, make it public so anyone with the URL can access it.

The HTML files run client-side inside embedded components. They do not require additional Python libraries.

## Notes

- The app uses a fixed starting height for each lab. If a lab appears cut off, increase that lab's `height` value in `app.py`.
- Test each simulation after deployment, especially buttons, tabs, canvas plots, and quizzes.
- This setup does not add login, user accounts, progress tracking, or a database. Those would need to be added separately.
