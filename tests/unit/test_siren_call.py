from app.siren_call import parse_build_event


class TestSirenCall:
    def test_can_parse_cloud_watch_event(self):
        # Arrange
        build_detail = {
            "build-status": "IN_PROGRESS",
            "project-name": "flask_bootstrap",
        }

        build_event = {"detail": build_detail}

        # Act
        project, status = parse_build_event(build_event)

        # Assert
        assert project == "flask_bootstrap"
        assert status == "IN_PROGRESS"
