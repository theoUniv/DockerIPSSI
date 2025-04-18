FROM mysql:8.0

EXPOSE 5655

HEALTHCHECK --interval=10s --timeout=3s --start-period=5s \
    CMD mysqladmin ping -h localhost -P 5655 --silent

CMD ["--port=5655"]
