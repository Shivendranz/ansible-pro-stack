FROM python:3.10-alpine

# 1. Directory set karo
WORKDIR /code

# 2. Environment variables (Flask ke liye zaroori)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# 3. Pehle sirf requirements copy karo (Caching ke liye)
# Iska fayda: Agar aap sirf code badalte ho, toh 'pip install' baar-baar nahi chalega
COPY requirements.txt requirements.txt

# 4. Dependencies install karo
RUN pip install --no-cache-dir -r requirements.txt

# 5. Ab baaki ka code copy karo
COPY . .

# 6. Port expose
EXPOSE 5000

# 7. App start karo
CMD ["flask", "run"]
