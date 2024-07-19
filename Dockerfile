FROM python
WORKDIR /app
COPY . . 
COPY /BANK /app/
CMD ["python", "BANK/MainApp.py"]
