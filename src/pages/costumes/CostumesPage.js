import React, { useEffect, useState } from "react";

import { Col, Row, Container } from "react-bootstrap";

import Costume from "./Costume";
import Asset from "../../components/Asset";

import appStyles from "../../App.module.css";
import { useLocation } from "react-router";
import { axiosReq } from "../../api/axiosDefaults";

import NoResults from "../../assets/no-results.png";
import InfiniteScroll from "react-infinite-scroll-component";
import { fetchMoreData } from "../../utils/utils";

function CostumesPage({ message, filter = "" }) {
  const [costumes, setCostumes] = useState({ results: [] });
  const [hasLoaded, setHasLoaded] = useState(false);
  const { pathname } = useLocation();

  useEffect(() => {
    const fetchCostumes = async () => {
      try {
        const { data } = await axiosReq.get(`/costumes/?${filter}`);
        setCostumes(data);
        setHasLoaded(true);
      } catch (err) {
        console.log(err);
      }
    };

    setHasLoaded(false);
    fetchCostumes();
  }, [filter, pathname]);

  return (
    <Row className="h-100">
      <Col className="py-2 p-0 p-lg-2" lg={8}>
        <p>Popular profiles mobile</p>
        {hasLoaded ? (
          <>
            {costumes.results.length ? (
              <InfiniteScroll
              children={costumes.results.map((costume) => (
                <Costume key={costume.id} {...costume} setCostumes={setCostumes} />
              ))}
              dataLength={costumes.results.length}
              loader={<Asset spinner />}
              hasMore={!!costumes.next}
              next={() => fetchMoreData(costumes, setCostumes)}
            />
            ) : (
              <Container className={appStyles.Content}>
                <Asset src={NoResults} message={message} />
              </Container>
            )}
          </>
        ) : (
          <Container className={appStyles.Content}>
            <Asset spinner />
          </Container>
        )}
      </Col>
      <Col md={4} className="d-none d-lg-block p-0 p-lg-2">
        <p>Popular profiles for desktop</p>
      </Col>
    </Row>
  );
}

export default CostumesPage;