(ns aoc2015.day2-test
  (:require [clojure.test :refer :all])
  (:require [aoc2015.day2 :refer :all]))

(def puzzle-input (slurp "resources/day2.txt"))

(deftest wrapping-paper-test
  (testing "wrapping-paper"
    (is (= (wrapping-paper 2 3 4) 58))
    (is (= (wrapping-paper 1 1 10) 43))
    )
  )

(deftest part1-test
  (testing "part1"
    (is (= (part1 puzzle-input) 1606483))
    )
  )

(deftest smallest-perimeter-test
  (testing "smallest-perimeter"
    (is (= (smallest-perimeter 2 3 4) 10))
    (is (= (smallest-perimeter 1 1 10) 4))
    )
  )

(deftest part2-test
  (testing "part2"
    (is (= (part2 puzzle-input) 3842356))
    )
  )
