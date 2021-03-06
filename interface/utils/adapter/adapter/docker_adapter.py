class DockerAdapter(object):
   def getInstances(self, prefix):
        return "docker container ls --format '{{.Names}}' | grep '" + prefix + "'"

   def stopInstance(self, containerName):
        return "docker exec '{}' pkill -int ffmpeg &".format(containerName)

   def startInstance(self, media_path, containerName, title, limit_in_gb, imageName, UID, GID, resolution):
        return "docker run -d -e LIMIT_MAXIMUM_FOLDER_GB={} -e UID={} -e GID={} --rm -v {}:/code/videos/ --name {} {} /code/recorder.sh -u https://chaturbate.com/{}/ -c {} -r {} &".format(
            limit_in_gb,
            UID,
            GID,
            media_path, 
            containerName, 
            imageName,
            title,
            containerName,
            resolution
        )
