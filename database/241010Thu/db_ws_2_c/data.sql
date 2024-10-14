-- Active: 1728876494429@@127.0.0.1@3306

SELECT BillingCountry, SUM(Total) AS TotalSales 
FROM invoices 
GROUP BY BillingCountry;

SELECT strftime('%Y', InvoiceDate) AS Year, SUM(Total) AS TotalSales 
FROM invoices 
GROUP BY Year;

SELECT BillingState, SUM(Total) AS TotalSales 
FROM invoices 
WHERE BillingCountry = 'USA' AND InvoiceDate >= '2010-01-01' 
GROUP BY BillingState;

SELECT BillingCountry, MAX(Total) AS MaxOrderAmount 
FROM invoices 
WHERE BillingCountry IN ('Germany', 'France') 
GROUP BY BillingCountry;