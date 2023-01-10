(ns aoc2015.day1_test
  (:require [clojure.test :refer :all]
            [aoc2015.day1 :refer :all]))

(def puzzle-input (slurp "resources/day1.txt"))

(deftest parse-test
  (testing "parse"
    (is (= (parse-floor-diffs "(") [1]))
    (is (= (parse-floor-diffs ")") [-1]))
    (is (= (parse-floor-diffs "()") [1 -1]))
    (is (= (parse-floor-diffs "()(") [1 -1 1]))
    ))

(deftest goto-test
  (testing "goto"
    (is (= (goto 0 [1]) 1))
    (is (= (goto 0 [1 1 1]) 3))
    (is (= (goto 0 [-1]) -1))
    (is (= (goto 0 [-1 1]) 0))
    )
  )

(deftest part1-test
  (testing "part1"
    (is (= (part1 "(())") 0))
    (is (= (part1 "(()(()(") 3))
    (is (= (part1 ")())())") -3))
    (is (= (part1 puzzle-input) 232))
    )
  )

(deftest part2-test
  (testing "part2"
    (is (= (part2 ")") 1))
    (is (= (part2 "()())") 5))
    (is (= (part2 puzzle-input) 1783))
    )
  )
