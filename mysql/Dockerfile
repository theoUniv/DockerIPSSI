FROM mysql:8.0



EXPOSE 3306
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s \
    CMD mysqladmin ping -h localhost --silent
