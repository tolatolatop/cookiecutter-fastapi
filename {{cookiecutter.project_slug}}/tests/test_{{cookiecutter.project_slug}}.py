#!/usr/bin/env python
"""Tests for `{{cookiecutter.project_slug}}` package."""
import pytest


@pytest.fixture
def client():
    from {{cookiecutter.project_slug}} import {{cookiecutter.project_slug}}
    from fastapi.testclient import TestClient

    return TestClient({{cookiecutter.project_slug}}.app)


def test_root(client):
    """Sample pytest test function with the pytest fixture as an argument."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_healthz(client):
    """Sample pytest test function with the pytest fixture as an argument."""
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}


def test_all_endpoints_have_tests():
    from {{cookiecutter.project_slug}} import {{cookiecutter.project_slug}}

    # 检查所有的测试方法是否以“test_”开头
    test_methods = [
        f"/{item.__name__}"
        for item in globals().values()
        if callable(item) and item.__name__.startswith("test_")
    ]

    endpoints = [
        method.replace("test_", "").replace("_", "/")
        for method in test_methods
        if method != "test_all_endpoints_have_tests"
    ]

    endpoints.append("/") if "/root" in endpoints else None
    endpoints.append("/openapi.json")
    endpoints.append("/docs")
    endpoints.append("/docs/oauth2-redirect")
    endpoints.append("/redoc")

    # 获取所有的接口路径和方法
    routes = [
        route.path for route in {{cookiecutter.project_slug}}.app.routes if hasattr(route, "methods")
    ]

    # 断言每个接口路径是否出现在测试方法中
    for route in routes:
        assert route in endpoints
