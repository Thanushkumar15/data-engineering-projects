from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col

spark = SparkSession.builder.appName("SpotifyPlaylistTransform").getOrCreate()

raw_path = "s3://spotify-etl-pipeline-2025/raw/spotify_playlists/"
output_path = "s3://spotify-etl-pipeline-2025/structured/spotify_playlists/"

df = spark.read.json(raw_path)
tracks = df.select(explode(col("tracks.items")).alias("item"))
tracks_flat = tracks.select(
    col("item.track.id").alias("track_id"),
    col("item.track.name").alias("track_name"),
    col("item.track.popularity").alias("popularity"),
    col("item.track.album.name").alias("album_name"),
    col("item.track.artists")[0]["name"].alias("artist_name"),
    col("item.added_at").alias("added_at")
)
tracks_flat.write.mode("overwrite").parquet(output_path)
