# Mapare de certificate cu nume de domeniu

Identificați cărui domeniu aparține fiecare certificat (`cert-....pem`).
Folosiți o comandă de forma:

```
openssl x509 -in cert-0.pem -noout -text | grep '\(Subject\|DNS\)'
```
