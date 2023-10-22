import React from "react";
import styles from "../../styles/Costume.module.css";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import { Card, Media, OverlayTrigger, Tooltip } from "react-bootstrap";
import { Link } from "react-router-dom";
import Avatar from "../../components/Avatar";
import { axiosRes } from "../../api/axiosDefaults";

const Costume = (props) => {
  const {
    id,
    owner,
    profile_id,
    profile_image,
    votes_count,
    vote_id,
    title,
    content,
    image,
    updated_at,
    setCostumes,
  } = props;

  const currentUser = useCurrentUser();
  const is_owner = currentUser?.username === owner;

  const handleVote = async () => {
    try {
      const { data } = await axiosRes.costume("/votes/", { costume: id });
      setCostumes((prevCostumes) => ({
        ...prevCostumes,
        results: prevCostumes.results.map((costume) => {
          return costume.id === id
            ? { ...costume, votes_count: costume.votes_count + 1, vote_id: data.id }
            : costume;
        }),
      }));
    } catch (err) {
      console.log(err);
    }
  };

  const handleUnvote = async () => {
    try {
      await axiosRes.delete(`/votes/${vote_id}/`);
      setCostumes((prevCostumes) => ({
        ...prevCostumes,
        results: prevCostumes.results.map((costume) => {
          return costume.id === id
            ? { ...costume, votes_count: costume.votes_count - 1, vote_id: null }
            : costume;
        }),
      }));
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <Card className={styles.Costume}>
      <Card.Body>
        <Media className="align-items-center justify-content-between">
          <Link to={`/profiles/${profile_id}`}>
            <Avatar src={profile_image} height={55} />
            {owner}
          </Link>
          <div className="d-flex align-items-center">
            <span>{updated_at}</span>
            {is_owner && "..."}
          </div>
        </Media>
      </Card.Body>
      <Link to={`/costumes/${id}`}>
        <Card.Img src={image} alt={title} />
      </Link>
      <Card.Body>
        {title && <Card.Title className="text-center">{title}</Card.Title>}
        {content && <Card.Text>{content}</Card.Text>}
        <div className={styles.CostumeBar}>
          {is_owner ? (
            <OverlayTrigger
              placement="top"
              overlay={<Tooltip>You can't vote for your own costumes!</Tooltip>}
            >
              <i className="far fa-heart" />
            </OverlayTrigger>
          ) : vote_id ? (
            <span onClick={handleUnVote}>
              <i className={`fas fa-heart ${styles.Heart}`} />
            </span>
          ) : currentUser ? (
            <span onClick={handleVote}>
              <i className={`far fa-heart ${styles.HeartOutline}`} />
            </span>
          ) : (
            <OverlayTrigger
              placement="top"
              overlay={<Tooltip>Log in to vote!</Tooltip>}
            >
              <i className="far fa-heart" />
            </OverlayTrigger>
          )}
          {votes_count}
          <Link to={`/costumes/${id}`}>
            <i className="far fa-comments" />
          </Link>
          {comments_count}
        </div>
      </Card.Body>
    </Card>
  );
};

export default Costume;