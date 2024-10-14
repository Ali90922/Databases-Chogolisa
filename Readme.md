# Databases-Chogolisa

![Alt text](Chogolisa.jpg)


# Database Concepts and Design

This document provides an overview of essential database concepts, definitions, and normalization techniques.

## Purpose of a Database
Databases offer the following key benefits:
- **Decoupling:** Separates data storage from application logic.
- **Data Integrity:** Ensures data accuracy and reliability.
- **Concurrency:** Allows multiple users to access data simultaneously.
- **Backups & Recovery:** Provides mechanisms to restore data in case of failure.
- **Security:** Protects data from unauthorized access.
- **Abstractions:** Simplifies data representation.
- **ACID Properties:** Guarantees reliable transactions.
  - **Atomicity** – All parts of a transaction succeed or none do.
  - **Consistency** – Only valid data is written to the database.
  - **Isolation** – Transactions do not interfere with each other.
  - **Durability** – Data remains once a transaction is committed.

## Types of Attributes
- **Atomic:** Single, indivisible values.
- **Composite:** Made up of multiple atomic attributes.
- **Multivalued:** Attributes that can have multiple values.
- **Derived:** Computed based on other attributes.

## Entity-Relationship (ER) Modeling
1. **Keys:**
   - **Key** – Identifies every entity in an entity set uniquely.
   - **Superkey** – A set of attributes uniquely identifying entities.
   - **Candidate Key (Minimal Superkey)** – A superkey with no redundant attributes.
   - **Primary Key** – The chosen candidate key for entity identification.
   
2. **Relationships:**
   - **Cardinalities:** Define the number of instances involved in relationships.
   - **Participation Constraints:** Whether every entity in a set must participate in a relationship.
   - **Unary/Ternary Relationships:** Self-referencing (unary) and three-entity relationships (ternary).

3. **Weak Entities:** Entities that depend on a strong entity, identified using a partial key and the strong entity’s key.

## Converting ER/EER Diagrams to Relational Models
- Handle **subclasses** by creating separate tables with foreign keys referencing the superclass.
- Manage **weak entities** by including a foreign key to the strong entity.
- Translate **multi-valued attributes** into new tables.
- **Unary relationships:** Use foreign keys referencing the same table.

## Relational Model Terms
- **Relation Schema:** Structure of a table.
- **Instance:** Actual table data.
- **Degree:** Number of attributes in a relation.
- **Cardinality:** Number of tuples in a relation.

## SQL Commands
- **Data Definition Language (DDL):**
  - `CREATE TABLE`, `ALTER`, `DROP`
- **Data Manipulation Language (DML):**
  - `INSERT`, `SELECT`, `UPDATE`, `DELETE`
  - Use clauses such as `WHERE`, `BETWEEN`.

## Functional Dependencies (FD) and Normalization
- **Functional Dependency:** When one attribute uniquely determines another.
- **Normalization:** Process of organizing data to reduce redundancy.
  - **BCNF (Boyce-Codd Normal Form):** Eliminate anomalies by ensuring all non-trivial FDs point to superkeys.

### Proving Functional Dependencies
- **Axioms and Corollaries** for proving or disproving FDs.
- **Normalization Steps:** Identify keys, dependencies, and normalize tables.

