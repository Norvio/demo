FROM python:3.13-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
RUN python -m pip uninstall -y pip \
 && useradd --uid 10001 --no-create-home app
COPY --from=build /install /usr/local
COPY worker.py .
USER 10001
EXPOSE 9000
CMD ["python", "worker.py"]