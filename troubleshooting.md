# Troubleshooting Log


## Database

### Issue 001: No migrations to apply.

When running the command:

    python manage.py migrate

If "No migrations to apply" gets printed to the terminal, then drop the existing table by running:

    python manage.py migrate NAME_OF_YOUR_APP zero

Then finally run again:

    python manage.py migrate

---

### Issue 002: django.db.utils.IntegrityError: (1048)

1 - Drop tables

2 - Comment-out the model in models.py

3 - Run

    python manage.py makemigrations
    python manage.py migrate --fake

4 - Comment-in your model in models.py

5 - Go to step 3. BUT this time without --fake
