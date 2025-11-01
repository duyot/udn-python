This repository is the learning patch for python programming

# Core Python Fundamentals

## Object-Oriented Programming

  - Classes and inheritance - Used extensively in entity models (memory/entity/)
  - Abstract base classes - See memory/entity/base.py and memory/cache/base.py
  - Multiple inheritance - Entity classes inherit from both SQLAlchemy and custom bases
  - Class methods and static methods - Factory pattern in memory/factory.py
  - Properties and descriptors - Used in entity serialization

## Advanced Python Concepts

  - Decorators - Celery tasks use @app.task, @shared_task decorators
  - Context managers - Database connections use with statements
  - Generators and iterators - Document processing pipelines
  - Type hints - Modern Python typing throughout the codebase
  - Async/await - Some components use asyncio patterns

  ## Web Development with Flask

  Flask Framework

  - Application factory pattern - See api/run_localGPT_API.py
  - Blueprints - Modular API organization in api/blueprints/
  - Request handling - POST/GET endpoints, JSON processing
  - CORS (Cross-Origin Resource Sharing) - API accessibility
  - Error handling - Custom error responses and status codes

  REST API Design

  - HTTP methods - GET, POST for different operations
  - JSON serialization/deserialization - Request/response handling
  - Authentication middleware - Security utilities in api/utils/security.py
  - Request validation - Input sanitization and validation

  ## Database Programming

  SQLAlchemy ORM

  - Model definition - Entity classes with SQLAlchemy tables
  - Relationships - Foreign keys, one-to-many, many-to-many
  - Session management - Database transactions and connection pooling
  - Query building - Complex database queries
  - Migrations - Schema changes and database initialization

  MongoDB with PyMongo

  - Document-based storage - NoSQL data modeling
  - Query operations - Find, insert, update operations
  - Aggregation pipelines - Complex data processing
  - Connection management - MongoDB client handling

Database Abstraction

  - Repository pattern - Data access layer abstraction
  - Factory pattern - Service creation and dependency injection
  - Singleton pattern - Database connection management in memory/database/db_instance.py

  ## Asynchronous Programming

  Celery Distributed Tasks

  - Task definition - @celery_app.task decorators
  - Task queues - Background job processing
  - Result backends - Task result storage
  - Worker management - Scaling and monitoring
  - Error handling and retries - Robust task execution

## Async Patterns

  - Background processing - Document ingestion tasks
  - Event-driven architecture - Task callbacks and notifications
  - Concurrency - Multiple workers and parallel processing

## AI/ML Integration

  LangChain Framework

  - Document loaders - PDF processing and text extraction
  - Text splitters - Document chunking strategies
  - Vector stores - ChromaDB integration for similarity search
  - Retrieval chains - RAG (Retrieval-Augmented Generation) pipelines
  - Prompt templates - Dynamic prompt generation

  Vector Databases

  - ChromaDB - Vector storage and similarity search
  - Embeddings - Text-to-vector conversion
  - Semantic search - Document retrieval based on meaning

## Configuration Management

Environment-Based Configuration

  - YAML processing - Configuration file parsing
  - Environment variables - Runtime configuration
  - Multi-environment setup - dev/prod/local configurations
  - Configuration validation - Ensuring required settings

  Dependency Injection

  - Service factory pattern - memory/factory.py
  - Configuration-driven instantiation - Services based on config
  - Singleton pattern - Shared instances

## Debugging

  - Python debugger (pdb) - Interactive debugging
  - Logging - Structured logging with Python's logging module
  - Error tracking - Exception handling and reporting

## Package Management

Python Packaging

  - requirements.txt - Dependency specification
  - Virtual environments - Isolated Python environments
  - conda - Environment and package management
  - pip - Package installation