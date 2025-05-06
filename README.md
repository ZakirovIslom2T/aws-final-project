Here's a **step-by-step guide** to run your full AWS-based application that connects **S3 (static site)**, **EC2 (backend)**, and **RDS PostgreSQL**:

---

## ✅ **Step-by-Step Instructions**

---

### 🟢 1. **Launch Backend (Flask App) on EC2**

**SSH into EC2:**

```bash
ssh -i "C:\Users\Islam\Downloads\rds--islam.pem" ubuntu@ec2-3-110-28-118.ap-south-1.compute.amazonaws.com
```

**Activate virtual environment:**

```bash
source venv/bin/activate
```

**Run your Flask app:**

```bash
python3 app.py
```

Make sure your Flask app includes:

```python
app.run(host='0.0.0.0', port=5000, debug=True)
```

🔒 **Security Group must allow:**

* Inbound rule for port `5000` (Custom TCP or All traffic)

✅ **Test it**:
In your browser, open:

```
http://3.110.28.118:5000/data
```

You should see JSON output from your RDS database.

---

### 🟢 2. **Upload & Serve HTML via S3**

1. Open AWS Console → S3 → Create a bucket (enable static website hosting).
2. Upload your `index_islam.html` file.
3. Make it public (or use a bucket policy).
4. Note the **S3 static website URL** (e.g.):

   ```
   http://[<your-bucket>.s3-website-<region>.amazonaws.com](http://islam-2t.s3-website.ap-south-1.amazonaws.com/)
   ```

✅ Visit the link — your HTML page should load with buttons and fetch/display data.

---

### 🟢 3. **Ensure RDS Is Accessible**

* RDS PostgreSQL must:

  * Be publicly accessible.
  * Have a **Security Group** allowing inbound access from your EC2 **private IP**.
  * Credentials in `app.py` must be correct:

    ```python
    psycopg2.connect(
        host="your-rds-endpoint",
        database="db_islam",
        user="postgres",
        password="postgres",
        port="5432"
    )
    ```

---

### 🟢 4. **Verify Functionality**

* ✅ Add data: Fill form, click **Add** → New row appears
* ✅ Delete data: Enter App ID, click **Delete** → Row removed
* ✅ Data should be real-time, connected to your RDS

---

### 🟢 5. **Optional: Keep Backend Running**

Use `tmux` or `nohup` to keep Flask running even after logout:

```bash
nohup python3 app.py &
```

---

S3 Bucket: https://ap-south-1.console.aws.amazon.com/s3/buckets/islam-2t?region=ap-south-1&tab=objects&bucketType=general
EC2 Instance: https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#InstanceDetails:instanceId=i-0e38785bc769ae2fc
RDS Database: https://ap-south-1.console.aws.amazon.com/rds/home?region=ap-south-1#database:id=rds-islam;is-cluster=false
